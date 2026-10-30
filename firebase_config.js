/**
 * TelTech 5G FWA E-Tender Portal — Firebase Centralized Backend
 * Project: g-fwa-rfp
 * Author: OLIVER TUNGOL, PMP, PECE (oliver.tungol@comclark.com.ph)
 */

(function(window) {
  const firebaseConfig = {
    apiKey: "AIzaSyCaU6dvX030b6xOy13Qm3MiCp6pLwEkih0",
    authDomain: "g-fwa-rfp.firebaseapp.com",
    projectId: "g-fwa-rfp",
    storageBucket: "g-fwa-rfp.firebasestorage.app",
    messagingSenderId: "736184704688",
    appId: "1:736184704688:web:d9b8fbd146c91885a86575"
  };

  if (typeof firebase !== 'undefined') {
    if (!firebase.apps.length) {
      firebase.initializeApp(firebaseConfig);
    }
    window.fwaFirebaseApp = firebase.app();
    window.fwaAuth = firebase.auth();
    window.fwaDb = firebase.firestore();
  } else {
    console.warn("Firebase SDK not loaded on this page.");
  }

  window.FWA_FIREBASE_CONFIG = firebaseConfig;
})(window);
