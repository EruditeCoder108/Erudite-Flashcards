package com.erudite.flashcards;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class ReleaseConfigurationTest {

    @Test
    public void releaseIdentityRemainsStable() {
        assertEquals("com.erudite.flashcards", BuildConfig.APPLICATION_ID);
        assertEquals(2, BuildConfig.VERSION_CODE);
        assertEquals("2.0", BuildConfig.VERSION_NAME);
    }
}
