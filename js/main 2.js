(function () {
  "use strict";

  var toggle = document.querySelector(".nav-toggle");
  var mobileNav = document.querySelector(".nav-mobile");
  if (toggle && mobileNav) {
    toggle.addEventListener("click", function () {
      var open = toggle.getAttribute("aria-expanded") === "true";
      toggle.setAttribute("aria-expanded", String(!open));
      mobileNav.classList.toggle("is-open", !open);
    });
    mobileNav.querySelectorAll('a[href^="#"]').forEach(function (link) {
      link.addEventListener("click", function () {
        toggle.setAttribute("aria-expanded", "false");
        mobileNav.classList.remove("is-open");
      });
    });
  }

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
