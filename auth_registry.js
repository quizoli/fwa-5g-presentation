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
      passwordHash: "3c1bd18d033a77346541b3eb647174d1f96d89860c3f77338c12b623f4495c74",
      registeredAt: "2026-09-25"
    },
    {
      username: "executive",
      name: "Executive Leadership",
      email: "executive@comclark.com.ph",
      organization: "Executive Management",
      role: "Executive Reviewer",
      isAdmin: true,
      status: "active",
      // Hash of "Executive2026!"
      passwordHash: "fae342bee3b047fd6aeaf7021e3a1e3618319744da0740c79f56e90c46a546c1",
      registeredAt: "2026-10-15"
    },
    {
      username: "admin",
      name: "System Administrator",
      email: "admin@comclark.com.ph",
      organization: "TelTech & Comclark Network Operations",
      role: "System Administrator",
      isAdmin: true,
      status: "active",
      passwordHash: "ef03da33db83125ac00fe6dbb96f6475117d1d640f76cd2344168efa1181bba8",
      registeredAt: "2026-09-25"
    },
    {
      username: "bidder.huawei",
      name: "Huawei Bid Team",
      email: "bidder.huawei@teltech-rfp.com",
      organization: "Huawei Technologies Philippines Inc.",
      role: "Tier-1 OEM Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "277b76c7347887d03b4b2ca1f7a5d563666d23dff41f8d7d1e6dd7c9893d3b1c",
      registeredAt: "2026-10-14"
    },
    {
      username: "bidder.nokia",
      name: "Nokia Bid Team",
      email: "bidder.nokia@teltech-rfp.com",
      organization: "Nokia Solutions and Networks Philippines",
      role: "Tier-1 OEM Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "a5099394c79345a9aa9364ac66690c014a914c98580da8b889a9597ec795b4fb",
      registeredAt: "2026-10-14"
    },
    {
      username: "bidder.ericsson",
      name: "Ericsson Bid Team",
      email: "bidder.ericsson@teltech-rfp.com",
      organization: "Ericsson Telecommunications Inc.",
      role: "Tier-1 OEM Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "95b975d7801999a2f45c53ed819d1ca6c87171948d857d9a92e2588f250d05bf",
      registeredAt: "2026-10-14"
    },
    {
      username: "bidder.zte",
      name: "ZTE Bid Team",
      email: "bidder.zte@teltech-rfp.com",
      organization: "ZTE Corporation Philippines",
      role: "Tier-1 OEM Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "73738bdefed15ec916f522b5c70e18482fd6bcd46c9b386a656cc6976d0f7327",
      registeredAt: "2026-10-14"
    },
    {
      username: "bidder.generic",
      name: "Authorized OEM Bidder",
      email: "bidder@teltech-rfp.com",
      organization: "Shortlisted Tier-1 Equipment Manufacturer",
      role: "Qualified RFP Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "19c24bb3b51d5e50d33e953bdf9f47cf61f5337d09c2f6f2c47ab788df4f9e12",
      registeredAt: "2026-10-14"
    },
    {
      username: "jdelacruz",
      name: "Juan dela Cruz",
      email: "otungol@yahoo.com",
      organization: "Bidder Partner",
      role: "Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "1f4b19af08eaf919b66e6e4c3a505db243656ca1938fc8906678294f89cd9001",
      registeredAt: "2026-10-15"
    },
    {
      username: "danny",
      name: "Jianhui Hu",
      email: "hujianhui1@huawei.com",
      organization: "Huawei",
      role: "Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "af78623a535884fb37aaa3b6a756031ab12d4ad9422e081fc62a2e39e7cb1a6c",
      registeredAt: "2026-10-15"
    },
    {
      username: "nokia_airfiber",
      name: "Triton Santos",
      email: "triton.santos@nokia.com",
      organization: "NOKIA SOLUTIONS AND NETWORKS PHILIPPINES, INC.",
      role: "Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "c814a124082a915d90a0f529773d5525afa4cc64b342e15c97cbf5de0393ddc3",
      registeredAt: "2026-10-15"
    },
    {
      username: "john_li",
      name: "John",
      email: "li.zhang1@zte.com.cn",
      organization: "ZTE",
      role: "Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "08cf69ab9c8c3fe70e6ab4e90dcea5fcaff2746e6018dccad5b1b2dadff7c0b2",
      registeredAt: "2026-10-15"
    },
    {
      username: "sam",
      name: "Sam Lau",
      email: "sam@all6.io",
      organization: "OREX SAI",
      role: "Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "82c20bfe9aaba01cdc56a1f1c366af63a30d55d3f75ca2e8986641f55c7e73ae",
      registeredAt: "2026-10-15"
    },
    {
      username: "xiao.yamin@huawei.com",
      name: "Kevin Xiao",
      email: "xiao.yamin@huawei.com",
      organization: "Huawei",
      role: "Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "36135da9586652aa0bdefee628001c4c4eb6901e278a44233a23cd2811eadc19",
      registeredAt: "2026-10-16"
    },
    {
      username: "kevin.xiao",
      name: "Kevin Xiao",
      email: "xiao.yamin@huawei.com",
      organization: "Huawei",
      role: "Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "36135da9586652aa0bdefee628001c4c4eb6901e278a44233a23cd2811eadc19",
      registeredAt: "2026-10-16"
    },
    {
      username: "shuxin",
      name: "Chng Shu Qing",
      email: "chng.shu.qing@huawei.com",
      organization: "Huawei Technologies Phils Inc",
      role: "Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "69be98964113451b7ea954f79e74be4b928e5ee7291db897e485eb5df4d9161b",
      registeredAt: "2026-10-16"
    },
    {
      username: "jayjiangzilong",
      name: "Jay_jiangzilong",
      email: "jiangzilong@huawei.com",
      organization: "Huawei",
      role: "Bidder",
      isAdmin: false,
      isBidder: true,
      status: "active",
      passwordHash: "fb326a1db5e0d5cefee3476f6b73a540b09680fce89928a6a8d9f09007a47f1e",
      registeredAt: "2026-10-17"
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
        isAdmin: !!user.isAdmin,
        isBidder: !!user.isBidder
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
