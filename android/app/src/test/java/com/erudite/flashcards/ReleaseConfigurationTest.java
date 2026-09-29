package com.erudite.flashcards;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class ReleaseConfigurationTest {

    // The application ID is the app's identity on Google Play and must never change.
    // The version code must rise with every upload, so it is only checked to be positive.
    @Test
    public void releaseIdentityRemainsStable() {
        assertEquals("com.erudite.flashcards", BuildConfig.APPLICATION_ID);
        assertTrue(BuildConfig.VERSION_CODE > 0);
    }
}
