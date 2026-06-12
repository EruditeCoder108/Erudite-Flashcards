param(
  [string]$SourceIcon = "assets/icons/icon.png"
)

$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.Drawing

$Root = Resolve-Path (Join-Path $PSScriptRoot "..")
$SourcePath = Join-Path $Root $SourceIcon
$ResPath = Join-Path $Root "android/app/src/main/res"

if (!(Test-Path $SourcePath)) {
  throw "Source icon not found: $SourcePath"
}

function New-Dir($Path) {
  if (!(Test-Path $Path)) {
    New-Item -ItemType Directory -Path $Path | Out-Null
  }
}

function Save-Png($Bitmap, $Path) {
  New-Dir (Split-Path $Path -Parent)
  $TempPath = "$Path.tmp.png"
  if (Test-Path $TempPath) {
    Remove-Item -LiteralPath $TempPath -Force
  }
  Write-Host "Saving $Path"
  $Bitmap.Save($TempPath, [System.Drawing.Imaging.ImageFormat]::Png)
  Move-Item -LiteralPath $TempPath -Destination $Path -Force
}

function New-RoundedRectPath($Rect, [float]$Radius) {
  $Path = New-Object System.Drawing.Drawing2D.GraphicsPath
  $Diameter = $Radius * 2
  $Path.AddArc($Rect.X, $Rect.Y, $Diameter, $Diameter, 180, 90)
  $Path.AddArc($Rect.Right - $Diameter, $Rect.Y, $Diameter, $Diameter, 270, 90)
  $Path.AddArc($Rect.Right - $Diameter, $Rect.Bottom - $Diameter, $Diameter, $Diameter, 0, 90)
  $Path.AddArc($Rect.X, $Rect.Bottom - $Diameter, $Diameter, $Diameter, 90, 90)
  $Path.CloseFigure()
  return $Path
}

function Draw-CenteredImage($Graphics, $Image, [int]$CanvasSize, [double]$Scale) {
  $TargetSize = [int]($CanvasSize * $Scale)
  $X = [int](($CanvasSize - $TargetSize) / 2)
  $Y = [int](($CanvasSize - $TargetSize) / 2)
  $Graphics.DrawImage($Image, $X, $Y, $TargetSize, $TargetSize)
}

function New-LauncherBitmap($Image, [int]$Size, [bool]$Round) {
  $Bitmap = New-Object System.Drawing.Bitmap $Size, $Size
  $Graphics = [System.Drawing.Graphics]::FromImage($Bitmap)
  $Graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $Graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $Graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
  $Graphics.Clear([System.Drawing.Color]::Transparent)

  $Rect = New-Object System.Drawing.RectangleF 0, 0, $Size, $Size
  if ($Round) {
    $Path = New-Object System.Drawing.Drawing2D.GraphicsPath
    $Path.AddEllipse($Rect)
  } else {
    $Path = New-RoundedRectPath $Rect ($Size * 0.24)
  }

  $Brush = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
    $Rect,
    [System.Drawing.ColorTranslator]::FromHtml("#111B2D"),
    [System.Drawing.ColorTranslator]::FromHtml("#07111F"),
    45
  )
  $Graphics.FillPath($Brush, $Path)
  Draw-CenteredImage $Graphics $Image $Size 0.68

  $Brush.Dispose()
  $Path.Dispose()
  $Graphics.Dispose()
  return $Bitmap
}

function New-ForegroundBitmap($Image, [int]$Size) {
  $Bitmap = New-Object System.Drawing.Bitmap $Size, $Size
  $Graphics = [System.Drawing.Graphics]::FromImage($Bitmap)
  $Graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $Graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $Graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
  $Graphics.Clear([System.Drawing.Color]::Transparent)
  Draw-CenteredImage $Graphics $Image $Size 0.72
  $Graphics.Dispose()
  return $Bitmap
}

function New-SplashBitmap($Image, [int]$Width, [int]$Height) {
  $Bitmap = New-Object System.Drawing.Bitmap $Width, $Height
  $Graphics = [System.Drawing.Graphics]::FromImage($Bitmap)
  $Graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
  $Graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
  $Graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
  $Graphics.Clear([System.Drawing.ColorTranslator]::FromHtml("#07111F"))

  $LogoSize = [int]([Math]::Min($Width, $Height) * 0.22)
  $X = [int](($Width - $LogoSize) / 2)
  $Y = [int](($Height - $LogoSize) / 2)
  $Graphics.DrawImage($Image, $X, $Y, $LogoSize, $LogoSize)

  $Graphics.Dispose()
  return $Bitmap
}

$Icon = [System.Drawing.Image]::FromFile($SourcePath)

$Densities = @{
  "mipmap-mdpi" = @{ launcher = 48; foreground = 108 }
  "mipmap-hdpi" = @{ launcher = 72; foreground = 162 }
  "mipmap-xhdpi" = @{ launcher = 96; foreground = 216 }
  "mipmap-xxhdpi" = @{ launcher = 144; foreground = 324 }
  "mipmap-xxxhdpi" = @{ launcher = 192; foreground = 432 }
}

foreach ($Name in $Densities.Keys) {
  $Dir = Join-Path $ResPath $Name
  $LauncherSize = $Densities[$Name].launcher
  $ForegroundSize = $Densities[$Name].foreground

  $Launcher = New-LauncherBitmap $Icon $LauncherSize $false
  Save-Png $Launcher (Join-Path $Dir "ic_launcher.png")
  $Launcher.Dispose()

  $Round = New-LauncherBitmap $Icon $LauncherSize $true
  Save-Png $Round (Join-Path $Dir "ic_launcher_round.png")
  $Round.Dispose()

  $Foreground = New-ForegroundBitmap $Icon $ForegroundSize
  Save-Png $Foreground (Join-Path $Dir "ic_launcher_foreground.png")
  $Foreground.Dispose()
}

$SplashTargets = @{
  "drawable" = @(1024, 1024)
  "drawable-port-mdpi" = @(480, 800)
  "drawable-port-hdpi" = @(720, 1200)
  "drawable-port-xhdpi" = @(960, 1600)
  "drawable-port-xxhdpi" = @(1440, 2400)
  "drawable-port-xxxhdpi" = @(1920, 3200)
  "drawable-land-mdpi" = @(800, 480)
  "drawable-land-hdpi" = @(1200, 720)
  "drawable-land-xhdpi" = @(1600, 960)
  "drawable-land-xxhdpi" = @(2400, 1440)
  "drawable-land-xxxhdpi" = @(3200, 1920)
}

foreach ($Name in $SplashTargets.Keys) {
  $Size = $SplashTargets[$Name]
  $Splash = New-SplashBitmap $Icon $Size[0] $Size[1]
  Save-Png $Splash (Join-Path (Join-Path $ResPath $Name) "splash.png")
  $Splash.Dispose()
}

$Icon.Dispose()
Write-Host "Android icon and splash assets generated."
