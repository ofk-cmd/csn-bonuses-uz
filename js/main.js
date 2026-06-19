(function () {
  "use strict";

  var toggle = document.querySelector(".nav-toggle");
  var mobileNav = document.querySelector(".nav-mobile");
  if (toggle && mobileNav) {
    function setNavOpen(open) {
      toggle.setAttribute("aria-expanded", String(open));
      mobileNav.classList.toggle("is-open", open);
      document.body.classList.toggle("nav-open", open);
    }
    toggle.addEventListener("click", function () {
      setNavOpen(toggle.getAttribute("aria-expanded") !== "true");
    });
    mobileNav.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        setNavOpen(false);
      });
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && mobileNav.classList.contains("is-open")) {
        setNavOpen(false);
      }
    });
  }

  document.querySelectorAll("[data-nav-disclosure]").forEach(function (wrap) {
    var btn = wrap.querySelector(".nav-mobile__disclosure-btn");
    var panel = wrap.querySelector(".nav-mobile__disclosure-panel");
    if (!btn || !panel) return;
    btn.addEventListener("click", function () {
      var open = btn.getAttribute("aria-expanded") === "true";
      btn.setAttribute("aria-expanded", String(!open));
      wrap.classList.toggle("is-open", !open);
      if (open) {
        panel.setAttribute("hidden", "");
      } else {
        panel.removeAttribute("hidden");
      }
    });
  });

  document.querySelectorAll(".nav-dropdown").forEach(function (dropdown) {
    var btn = dropdown.querySelector(".nav-dropdown__toggle");
    if (!btn) return;
    btn.addEventListener("click", function (event) {
      event.stopPropagation();
      var open = dropdown.classList.contains("is-open");
      document.querySelectorAll(".nav-dropdown.is-open").forEach(function (other) {
        if (other !== dropdown) {
          other.classList.remove("is-open");
          var otherBtn = other.querySelector(".nav-dropdown__toggle");
          if (otherBtn) otherBtn.setAttribute("aria-expanded", "false");
        }
      });
      dropdown.classList.toggle("is-open", !open);
      btn.setAttribute("aria-expanded", String(!open));
    });
  });

  document.addEventListener("click", function (event) {
    if (!event.target.closest(".nav-dropdown")) {
      document.querySelectorAll(".nav-dropdown.is-open").forEach(function (dropdown) {
        dropdown.classList.remove("is-open");
        var btn = dropdown.querySelector(".nav-dropdown__toggle");
        if (btn) btn.setAttribute("aria-expanded", "false");
      });
    }
  });

  var faqItems = document.querySelectorAll(".faq-item");
  faqItems.forEach(function (item, index) {
    var btn = item.querySelector(".faq-item__question");
    if (!btn) return;

    if (index === 0) {
      item.classList.add("is-open");
      btn.setAttribute("aria-expanded", "true");
    } else {
      btn.setAttribute("aria-expanded", "false");
    }

    btn.addEventListener("click", function () {
      var isOpen = item.classList.contains("is-open");
      faqItems.forEach(function (other) {
        other.classList.remove("is-open");
        var otherBtn = other.querySelector(".faq-item__question");
        if (otherBtn) otherBtn.setAttribute("aria-expanded", "false");
      });
      if (!isOpen) {
        item.classList.add("is-open");
        btn.setAttribute("aria-expanded", "true");
      }
    });
  });

  var backTop = document.querySelector(".back-to-top");
  if (backTop) {
    window.addEventListener("scroll", function () {
      backTop.classList.toggle("is-visible", window.scrollY > 600);
    });
    backTop.addEventListener("click", function () {
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  }

  var stickyCta = document.getElementById("sticky-cta");
  if (stickyCta) {
    document.body.classList.add("has-sticky-cta");
    var closeBtn = stickyCta.querySelector(".sticky-cta__close");
    if (closeBtn) {
      closeBtn.addEventListener("click", function () {
        stickyCta.classList.add("is-hidden");
        document.body.classList.remove("has-sticky-cta");
      });
    }
  }

  var copyPromoBtns = document.querySelectorAll(".js-copy-promo");
  copyPromoBtns.forEach(function (btn) {
    var defaultLabel = btn.textContent;
    btn.addEventListener("click", function (event) {
      event.preventDefault();
      event.stopPropagation();
      var targetId = btn.getAttribute("data-copy-target");
      var codeEl = targetId ? document.getElementById(targetId) : null;
      var code = codeEl ? codeEl.textContent.trim() : "";
      if (!code) return;

      function onCopied() {
        btn.classList.add("is-copied");
        btn.textContent = "Nusxalandi!";
        window.setTimeout(function () {
          btn.classList.remove("is-copied");
          btn.textContent = defaultLabel;
        }, 1800);
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(code).then(onCopied).catch(function () {
          window.prompt("Promo kodni nusxalang:", code);
        });
      } else {
        window.prompt("Promo kodni nusxalang:", code);
      }
    });
  });

})();
