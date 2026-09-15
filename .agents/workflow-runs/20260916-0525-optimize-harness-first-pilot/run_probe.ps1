param(
    [string]$RunRoot = (Split-Path -Parent $MyInvocation.MyCommand.Path)
)

$ErrorActionPreference = 'Stop'
$sourcePaths = @(
    'ai-native-builder/goals/g09-nang-cap-harness-rules-skills-workflows/README.md',
    '.agents/workflows/optimize-agent-harness-system.md',
    '.agents/decisions/2026-09-15-agent-harness-workflow-proposed.md'
)

function Get-Tokens([string]$Text) {
    $matches = [regex]::Matches($Text.ToLowerInvariant(), '[a-z0-9][a-z0-9_.\-/]{2,}')
    return @($matches | ForEach-Object Value | Sort-Object -Unique)
}

function Get-Overlap([string[]]$QueryTokens, [string[]]$DocumentTokens) {
    $set = @{}
    foreach ($token in $DocumentTokens) { $set[$token] = $true }
    return @($QueryTokens | Where-Object { $set.ContainsKey($_) } | Sort-Object -Unique).Count
}

function Get-BaselinePick([string]$Query) {
    $queryTokens = Get-Tokens $Query
    $scores = foreach ($path in $sourcePaths) {
        $content = Get-Content -Raw -Encoding utf8 $path
        [pscustomobject]@{ Path = $path; Score = Get-Overlap $queryTokens (Get-Tokens $content) }
    }
    $best = $scores | Sort-Object @{ Expression = 'Score'; Descending = $true }, @{ Expression = 'Path'; Descending = $false } | Select-Object -First 1
    if ($best.Score -lt 1) { return [pscustomobject]@{ Path = 'OUT_OF_SCOPE'; Score = $best.Score; Reads = $sourcePaths.Count } }
    return [pscustomobject]@{ Path = $best.Path; Score = $best.Score; Reads = $sourcePaths.Count }
}

function Get-CandidatePick([string]$Query, $Index) {
    $queryTokens = Get-Tokens $Query
    $scores = foreach ($entry in $Index.entries) {
        $keywordText = ($entry.keywords -join ' ')
        [pscustomobject]@{ Path = $entry.path; Score = Get-Overlap $queryTokens (Get-Tokens $keywordText) }
    }
    $best = $scores | Sort-Object @{ Expression = 'Score'; Descending = $true }, @{ Expression = 'Path'; Descending = $false } | Select-Object -First 1
    if ($best.Score -lt 2) { return [pscustomobject]@{ Path = 'OUT_OF_SCOPE'; Score = $best.Score; Reads = 0; SourceVerified = 0 } }
    $sourceContent = Get-Content -Raw -Encoding utf8 $best.Path
    $sourceEvidence = Get-Overlap $queryTokens (Get-Tokens $sourceContent)
    if ($sourceEvidence -lt 1) { return [pscustomobject]@{ Path = 'OUT_OF_SCOPE'; Score = $best.Score; Reads = 1; SourceVerified = 0 } }
    return [pscustomobject]@{ Path = $best.Path; Score = $best.Score; Reads = 1; SourceVerified = 1 }
}

$index = Get-Content -Raw -Encoding utf8 (Join-Path $RunRoot 'context-index.json') | ConvertFrom-Json
$rows = Import-Csv -Delimiter "`t" -Path (Join-Path $RunRoot 'query-set.tsv')
$results = foreach ($row in $rows) {
    $baseline = Get-BaselinePick $row.query
    $candidate = Get-CandidatePick $row.query $index
    [pscustomobject]@{
        Id = $row.id
        Class = $row.class
        Expected = $row.expected
        Baseline = $baseline.Path
        Candidate = $candidate.Path
        BaselineScore = $baseline.Score
        CandidateScore = $candidate.Score
        BaselineReads = $baseline.Reads
        CandidateReads = $candidate.Reads
        BaselineCorrect = [int]($baseline.Path -eq $row.expected)
        CandidateCorrect = [int]($candidate.Path -eq $row.expected)
        CandidateFalseAuthority = [int](($row.expected -eq 'OUT_OF_SCOPE') -and ($candidate.Path -ne 'OUT_OF_SCOPE'))
        CandidateSourceVerified = $candidate.SourceVerified
    }
}

$results | Export-Csv -NoTypeInformation -Encoding utf8 (Join-Path $RunRoot 'probe-results.csv')
$summary = [pscustomobject]@{
    QueryCount = $results.Count
    BaselineCorrect = ($results | Measure-Object BaselineCorrect -Sum).Sum
    CandidateCorrect = ($results | Measure-Object CandidateCorrect -Sum).Sum
    BaselineReads = ($results | Measure-Object BaselineReads -Sum).Sum
    CandidateReads = ($results | Measure-Object CandidateReads -Sum).Sum
    CandidateFalseAuthority = ($results | Measure-Object CandidateFalseAuthority -Sum).Sum
    CandidateSourceVerifications = ($results | Measure-Object CandidateSourceVerified -Sum).Sum
}
$summary | ConvertTo-Json | Set-Content -Encoding utf8 (Join-Path $RunRoot 'probe-summary.json')

$pathTitleFallback = $true
$linkIntegrity = $true
foreach ($path in $sourcePaths) {
    $pathTitleFallback = $pathTitleFallback -and (Test-Path $path) -and ((Select-String -Path $path -Pattern '^# ' -Encoding utf8 | Measure-Object).Count -gt 0)
    $content = Get-Content -Raw -Encoding utf8 $path
    $base = Split-Path $path
    foreach ($match in [regex]::Matches($content, '\[[^\]]+\]\(([^)]+)\)')) {
        $target = $match.Groups[1].Value.Split('#')[0]
        if ($target -and $target -notmatch '^(https?://|mailto:)') {
            $linkIntegrity = $linkIntegrity -and (Test-Path (Join-Path $base $target))
        }
    }
}
$schemaValid = $index.derived -eq $true -and $index.canonical -eq $false -and $index.entries.Count -eq 3
foreach ($entry in $index.entries) {
    $schemaValid = $schemaValid -and [bool]$entry.id -and [bool]$entry.path -and [bool]$entry.type -and [bool]$entry.authority -and [bool]$entry.status -and $entry.keywords.Count -gt 0 -and (Test-Path $entry.path)
}
[pscustomobject]@{
    PathTitleFallback = $pathTitleFallback
    LinkIntegrity = $linkIntegrity
    IndexSchema = $schemaValid
    RegressionPass = $pathTitleFallback -and $linkIntegrity -and $schemaValid
} | ConvertTo-Json | Set-Content -Encoding utf8 (Join-Path $RunRoot 'regression-results.json')
$results | Format-Table -AutoSize
$summary | Format-List
