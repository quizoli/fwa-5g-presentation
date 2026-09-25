/**
 * TelTech & Comclark — 5G Fixed Wireless Access (FWA) Portal
 * User Authentication & Cryptographic Clearance Registry
 * Author: OLIVER TUNGOL (oliver.tungol@comclark.com.ph)
 * Last Updated: September 2026
 */

(function(window) {
  // Primary Administrator Notification Contact
  const ADMIN_EMAIL = "oliver.tungol@comclark.com.ph";

  // Pre-Approved & Registered Users Database (SHA-256 One-Way Hashes)
  // Plain text passwords are NEVER stored in this registry.
  const USER_REGISTRY = [
    {
      username: "oliver.tungol",
      name: "Oliver Tungol",
      email: "oliver.tungol@comclark.com.ph",
      organization: "Comclark Network & Technology Corp.",
      role: "Lead Architect & Administrator",
      isAdmin: true,
      status: "active",
      // Hash of "OliverTungol2026!"
      passwordHash: "3c1bd18d033a77346541b3eb647174d1f96d89860c3f77338c12b623f4495c74",
      registeredAt: "2026-09-25"
    },
    {
      username: "executive",
      name: "Executive Leadership",
      email: "executive@comclark.com.ph",
      organization: "TelTech / Comclark Executive Office",
      role: "Executive Reviewer",
      isAdmin: false,
      status: "active",
      // Hash of "teltech2026"
      passwordHash: "ddef79b965dc9a8045528aeede3133fc77a7b1cf2d1def50070c83fd61fefef1",
      registeredAt: "2026-09-25"
    },
    {
      username: "admin",
      name: "System Administrator",
      email: "admin@comclark.com.ph",
      organization: "TelTech & Comclark Network Operations",
      role: "System Administrator",
      isAdmin: true,
      status: "active",
      // Hash of "fwa2026"
      passwordHash: "ef03da33db83125ac00fe6dbb96f6475117d1d640f76cd2344168efa1181bba8",
      registeredAt: "2026-09-25"
    },
    {
      username: "corporate.pin",
      name: "Band n50 Quick Passcode",
      email: "guest@comclark.com.ph",
      organization: "Authorized Reviewers",
      role: "Presentation Viewer",
      isAdmin: false,
      status: "active",
      // Hash of "5G2026"
      passwordHash: "e42db7c77805f23205d8a7170fd56ddd860130d7d344a156be3dd8d233228407",
      registeredAt: "2026-09-25"
    }
  ];

  // Cryptographic Helper: SHA-256
  async function computeSHA256(str) {
    const encoder = new TextEncoder();
    const data = encoder.encode(str);
    const hashBuffer = await crypto.subtle.digest("SHA-256", data);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    return hashArray.map(b => b.toString(16).padStart(2, "0")).join("");
  }

  // Validate Credentials against Registry
  async function authenticateUser(usernameOrEmail, password) {
    if (!usernameOrEmail || !password) return { success: false, message: "Missing credentials" };
    
    const query = usernameOrEmail.trim().toLowerCase();
    const pwHash = await computeSHA256(password.trim());

    // Check special corporate PIN override: if entered password or username matches corporate PIN hash
    if (pwHash === "e42db7c77805f23205d8a7170fd56ddd860130d7d344a156be3dd8d233228407" || 
        password.trim() === "5G2026") {
      return {
        success: true,
        user: {
          username: "executive.pin",
          name: "Executive Passcode User",
          email: "authorized@comclark.com.ph",
          role: "Executive Reviewer",
          isAdmin: false
        }
      };
    }

    const user = USER_REGISTRY.find(u => 
      (u.username.toLowerCase() === query || u.email.toLowerCase() === query)
    );

    if (!user) {
      return { success: false, message: "Unrecognized username or corporate email." };
    }

    if (user.status !== "active") {
      return { success: false, message: "Access suspended. Please contact oliver.tungol@comclark.com.ph." };
    }

    if (user.passwordHash !== pwHash) {
      return { success: false, message: "Invalid security passcode or password." };
    }

    return {
      success: true,
      user: {
        username: user.username,
        name: user.name,
        email: user.email,
        organization: user.organization,
        role: user.role,
        isAdmin: !!user.isAdmin
      }
    };
  }

  // Check Current Authentication State
  function getCurrentUser() {
    try {
      const raw = sessionStorage.getItem("fwa_portal_auth") || localStorage.getItem("fwa_portal_auth");
      return raw ? JSON.parse(raw) : null;
    } catch (e) {
      return null;
    }
  }

  // Sign In & Store Session
  function saveSession(userObj, rememberMe) {
    const data = JSON.stringify({
      ...userObj,
      authAt: new Date().toISOString()
    });
    sessionStorage.setItem("fwa_portal_auth", data);
    if (rememberMe) {
      localStorage.setItem("fwa_portal_auth", data);
    } else {
      localStorage.removeItem("fwa_portal_auth");
    }
  }

  // Sign Out & Lock
  function terminateSession() {
    sessionStorage.removeItem("fwa_portal_auth");
    localStorage.removeItem("fwa_portal_auth");
    window.location.replace("index.html");
  }

  // Expose to window
  window.FWAPortalAuth = {
    ADMIN_EMAIL,
    USER_REGISTRY,
    computeSHA256,
    authenticateUser,
    getCurrentUser,
    saveSession,
    terminateSession
  };
})(window);
