package com.erudite.flashcards;

import android.content.pm.ActivityInfo;
import android.content.res.Configuration;
import android.os.Bundle;
import android.webkit.WebView;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.webkit.WebSettingsCompat;
import androidx.webkit.WebViewFeature;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        androidx.core.splashscreen.SplashScreen splashScreen = androidx.core.splashscreen.SplashScreen.installSplashScreen(this);
        
        AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        registerPlugin(TactilePlugin.class);
        registerPlugin(SystemChromePlugin.class);
        super.onCreate(savedInstanceState);
        applyOrientationPolicy(getResources().getConfiguration());

        // Smoothly fade out the native splash screen over 250ms
        splashScreen.setOnExitAnimationListener(splashScreenViewProvider -> {
            splashScreenViewProvider.getView()
                .animate()
                .alpha(0f)
                .setDuration(250L)
                .withEndAction(() -> {
                    splashScreenViewProvider.remove();
                })
                .start();
        });

        // Fix system text-selection toolbar (Cut/Copy/Paste) colors
        // by disabling WebView algorithmic darkening
        try {
            WebView webView = getBridge().getWebView();
            if (webView != null) {
                if (WebViewFeature.isFeatureSupported(WebViewFeature.ALGORITHMIC_DARKENING)) {
                    WebSettingsCompat.setAlgorithmicDarkeningAllowed(webView.getSettings(), false);
                }
                // Text-only zoom from the system font size enlarges text inside
                // fixed-size boxes (rings, chips, buttons). The page scales its
                // whole layout from SystemChrome.getFontScale instead.
                webView.getSettings().setTextZoom(100);
            }
        } catch (Exception e) {
            // Non-critical: if WebView isn't ready yet, the theme fix alone should help
        }
    }

    @Override
    public void onConfigurationChanged(Configuration newConfig) {
        super.onConfigurationChanged(newConfig);
        // A foldable opened or closed changes the smallest width without
        // recreating the activity (see configChanges in the manifest).
        applyOrientationPolicy(newConfig);
    }

    /**
     * Phones stay in portrait: the layouts are built for a tall screen and
     * break in landscape. Tablets and unfolded foldables (smallest width of
     * 600dp or more) follow the device and have their own landscape layout.
     */
    private void applyOrientationPolicy(Configuration config) {
        int wanted = config.smallestScreenWidthDp >= 600
            ? ActivityInfo.SCREEN_ORIENTATION_FULL_USER
            : ActivityInfo.SCREEN_ORIENTATION_PORTRAIT;
        if (getRequestedOrientation() != wanted) setRequestedOrientation(wanted);
    }
}
