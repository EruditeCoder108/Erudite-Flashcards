package com.erudite.flashcards;

import android.os.Build;
import android.view.HapticFeedbackConstants;
import android.view.View;
import com.getcapacitor.Plugin;
import com.getcapacitor.PluginCall;
import com.getcapacitor.PluginMethod;
import com.getcapacitor.annotation.CapacitorPlugin;

/**
 * Short, system-tuned haptics through View.performHapticFeedback. Unlike raw
 * vibrator waveforms these match the phone's own keyboard and switch feel and
 * respect the system "touch feedback" setting.
 */
@CapacitorPlugin(name = "Tactile")
public class TactilePlugin extends Plugin {

    @PluginMethod
    public void perform(PluginCall call) {
        final int constant = constantFor(call.getString("kind", "tick"));
        final View view = getBridge().getWebView();
        if (view != null) {
            view.post(() -> view.performHapticFeedback(constant));
        }
        call.resolve();
    }

    static int constantFor(String kind) {
        final int sdk = Build.VERSION.SDK_INT;
        switch (kind == null ? "tick" : kind) {
            case "tap":
                return HapticFeedbackConstants.VIRTUAL_KEY;
            case "toggle-on":
                return sdk >= 34 ? HapticFeedbackConstants.TOGGLE_ON : HapticFeedbackConstants.CLOCK_TICK;
            case "toggle-off":
                return sdk >= 34 ? HapticFeedbackConstants.TOGGLE_OFF : HapticFeedbackConstants.CLOCK_TICK;
            case "threshold":
                if (sdk >= 34) return HapticFeedbackConstants.GESTURE_THRESHOLD_ACTIVATE;
                return sdk >= 23 ? HapticFeedbackConstants.CONTEXT_CLICK : HapticFeedbackConstants.VIRTUAL_KEY;
            case "confirm":
                return sdk >= 30 ? HapticFeedbackConstants.CONFIRM : HapticFeedbackConstants.VIRTUAL_KEY;
            case "reject":
                return sdk >= 30 ? HapticFeedbackConstants.REJECT : HapticFeedbackConstants.LONG_PRESS;
            case "long-press":
                return HapticFeedbackConstants.LONG_PRESS;
            case "tick":
            default:
                return HapticFeedbackConstants.CLOCK_TICK;
        }
    }
}
