package com.erudite.flashcards;

import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.view.Window;
import android.webkit.WebView;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;

/**
 * Paints the window, the status bar area and the navigation bar area in the
 * app's current background colour. Without it the native launch colour shows
 * as a band above and below the web content, which reads as a border when the
 * theme is not the same shade.
 */
@CapacitorPlugin(name = "SystemChrome")
public class SystemChromePlugin extends Plugin {

    @PluginMethod
    public void setColor(PluginCall call) {
        final int color;
        try {
            color = Color.parseColor(call.getString("color", "#0D0E10"));
        } catch (IllegalArgumentException error) {
            call.reject("Not a colour: " + call.getString("color"));
            return;
        }
        getActivity().runOnUiThread(() -> {
            Window window = getActivity().getWindow();
            window.setBackgroundDrawable(new ColorDrawable(color));
            window.getDecorView().setBackgroundColor(color);
            // Android 15+ draws edge to edge and ignores these; the window
            // background above then fills the bar areas instead.
            window.setStatusBarColor(color);
            window.setNavigationBarColor(color);
            WebView webView = getBridge().getWebView();
            if (webView != null) webView.setBackgroundColor(color);
            call.resolve();
        });
    }
}
