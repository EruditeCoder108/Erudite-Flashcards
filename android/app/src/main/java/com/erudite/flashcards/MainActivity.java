package com.erudite.flashcards;

import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebSettings;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.webkit.WebSettingsCompat;
import androidx.webkit.WebViewFeature;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        super.onCreate(savedInstanceState);

        // Fix system text-selection toolbar (Cut/Copy/Paste) colors
        // by disabling WebView algorithmic darkening
        try {
            WebView webView = getBridge().getWebView();
            if (webView != null) {
                webView.setForceDarkAllowed(false);

                if (WebViewFeature.isFeatureSupported(WebViewFeature.ALGORITHMIC_DARKENING)) {
                    WebSettingsCompat.setAlgorithmicDarkeningAllowed(webView.getSettings(), false);
                }
            }
        } catch (Exception e) {
            // Non-critical: if WebView isn't ready yet, the theme fix alone should help
        }
    }
}
