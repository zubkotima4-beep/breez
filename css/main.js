(function () {
  "use strict";

  const body = document.body;
  const header = document.querySelector(".header");
  const isOverlayHeader = header && header.classList.contains("header--overlay");

  /* ---------- Header, progress ---------- */
  const setScrollState = () => {
    if (!header) return;
    if (isOverlayHeader && !body.classList.contains("menu-open")) {
      header.classList.toggle("is-scrolled", window.scrollY > 40);
    }
    const doc = document.documentElement;
    const max = doc.scrollHeight - window.innerHeight;
    const progress = max > 0 ? Math.min(window.scrollY / max, 1) : 0;
    header.style.setProperty("--scroll-progress", progress.toFixed(4));
  };

  setScrollState();
  window.addEventListener("scroll", setScrollState, { passive: true });
  window.addEventListener("resize", setScrollState);

  /* ---------- Dropdown ---------- */
  document.querySelectorAll(".nav__item--has-dropdown").forEach((item) => {
    const trigger = item.querySelector(".nav__trigger");
    if (!trigger) return;

    trigger.addEventListener("click", (event) => {
      event.stopPropagation();
      const open = item.classList.toggle("is-open");
      trigger.setAttribute("aria-expanded", open ? "true" : "false");
      document.querySelectorAll(".nav__item--has-dropdown").forEach((other) => {
        if (other !== item) {
          other.classList.remove("is-open");
          const otherTrigger = other.querySelector(".nav__trigger");
          if (otherTrigger) otherTrigger.setAttribute("aria-expanded", "false");
        }
      });
    });
  });

  document.addEventListener("click", () => {
    document.querySelectorAll(".nav__item--has-dropdown.is-open").forEach((item) => {
      item.classList.remove("is-open");
      const trigger = item.querySelector(".nav__trigger");
      if (trigger) trigger.setAttribute("aria-expanded", "false");
    });
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      document.querySelectorAll(".nav__item--has-dropdown.is-open").forEach((item) => {
        item.classList.remove("is-open");
        const trigger = item.querySelector(".nav__trigger");
        if (trigger) trigger.setAttribute("aria-expanded", "false");
      });
    }
  });

  /* ---------- Mobile menu ---------- */
  const menuToggle = document.querySelector("[data-menu-toggle]");
  const mobileMenu = document.querySelector("[data-mobile-menu]");
  const mobileAccordions = document.querySelectorAll(".mobile-menu__accordion");

  const closeMenu = () => {
    body.classList.remove("menu-open", "no-scroll");
    if (menuToggle) menuToggle.setAttribute("aria-expanded", "false");
    if (mobileMenu) mobileMenu.setAttribute("aria-hidden", "true");
    setScrollState();
  };

  if (menuToggle) {
    menuToggle.addEventListener("click", () => {
      const isOpen = body.classList.toggle("menu-open");
      body.classList.toggle("no-scroll", isOpen);
      menuToggle.setAttribute("aria-expanded", isOpen ? "true" : "false");
      if (mobileMenu) mobileMenu.setAttribute("aria-hidden", isOpen ? "false" : "true");
      if (!isOpen) {
        mobileAccordions.forEach((accordion) => accordion.classList.remove("is-open"));
      }
    });
  }

  mobileAccordions.forEach((accordion) => {
    const button = accordion.querySelector("button");
    if (!button) return;
    button.addEventListener("click", () => {
      const open = accordion.classList.toggle("is-open");
      button.setAttribute("aria-expanded", open ? "true" : "false");
    });
  });

  if (mobileMenu) {
    mobileMenu.querySelectorAll("a").forEach((link) => {
      link.addEventListener("click", closeMenu);
    });
  }

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && body.classList.contains("menu-open")) closeMenu();
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 1024 && body.classList.contains("menu-open")) closeMenu();
  });

  /* ---------- Reveal ---------- */
  const revealItems = document.querySelectorAll("[data-reveal]");
  if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("is-visible");
          observer.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -8% 0px", threshold: 0.06 }
    );
    revealItems.forEach((item) => revealObserver.observe(item));
  } else {
    revealItems.forEach((item) => item.classList.add("is-visible"));
  }

  /* ---------- Toast ---------- */
  let toastTimer;
  const toast = document.createElement("div");
  toast.className = "toast";
  toast.setAttribute("role", "status");
  toast.setAttribute("aria-live", "polite");
  document.body.appendChild(toast);

  const showToast = (message) => {
    toast.textContent = message;
    toast.classList.add("is-visible");
    clearTimeout(toastTimer);
    toastTimer = setTimeout(() => toast.classList.remove("is-visible"), 2800);
  };

  /* ---------- Copy ---------- */
  const copyText = async (text) => {
    try {
      await navigator.clipboard.writeText(text);
      showToast("Скопировано");
      return true;
    } catch (error) {
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.style.position = "fixed";
      textarea.style.opacity = "0";
      document.body.appendChild(textarea);
      textarea.select();
      let ok = false;
      try {
        ok = document.execCommand("copy");
      } catch (e) {
        ok = false;
      }
      document.body.removeChild(textarea);
      showToast(ok ? "Скопировано" : "Не удалось скопировать");
      return ok;
    }
  };

  document.querySelectorAll("[data-copy]").forEach((button) => {
    button.addEventListener("click", () => {
      const target = button.getAttribute("data-copy");
      const source = target ? document.querySelector(target) : button.closest("[data-copy-value]");
      const text = target
        ? source && source.textContent.trim()
        : button.getAttribute("data-copy-value");
      if (text) copyText(text);
    });
  });

  /* ---------- Phone mask ---------- */
  document.querySelectorAll("[data-phone]").forEach((input) => {
    const format = (value) => {
      let digits = value.replace(/\D/g, "");
      if (!digits) return "";
      if (digits[0] === "8") digits = "7" + digits.slice(1);
      if (digits[0] !== "7") digits = "7" + digits;
      digits = digits.slice(0, 11);
      const p = digits.slice(1);
      let out = "+7";
      if (p.length) out += " (" + p.slice(0, 3);
      if (p.length >= 3) out += ")";
      if (p.length > 3) out += " " + p.slice(3, 6);
      if (p.length > 6) out += "-" + p.slice(6, 8);
      if (p.length > 8) out += "-" + p.slice(8, 10);
      return out;
    };

    input.addEventListener("input", () => {
      const atEnd = input.selectionStart === input.value.length;
      input.value = format(input.value);
      if (atEnd) input.setSelectionRange(input.value.length, input.value.length);
    });

    input.addEventListener("focus", () => {
      if (!input.value) input.value = "+7 (";
    });

    input.addEventListener("blur", () => {
      if (input.value === "+7 (" || input.value === "+7") input.value = "";
    });
  });

  /* ---------- Request dialog ---------- */
  const requestDialog = document.getElementById("requestDialog");
  const requestForm = requestDialog ? requestDialog.querySelector("[data-request-form]") : null;
  const successPanel = requestDialog ? requestDialog.querySelector("[data-request-success]") : null;
  const successText = requestDialog ? requestDialog.querySelector("[data-request-text]") : null;
  const requestMailto = requestDialog ? requestDialog.querySelector("[data-request-mailto]") : null;

  const openRequest = (source) => {
    if (!requestDialog) return;
    if (requestDialog.open) return;
    if (body.classList.contains("menu-open")) closeMenu();
    if (requestForm) {
      requestForm.reset();
      const phone = requestForm.querySelector("[data-phone]");
      if (phone) phone.value = "";
      if (successPanel) successPanel.classList.remove("is-visible");
      requestForm.hidden = false;
      const direction = requestForm.querySelector("[name='direction']");
      if (direction && source) {
        const label = source.getAttribute("data-request-topic");
        if (label) {
          Array.from(direction.options).forEach((option) => {
            if (option.value === label || option.textContent.trim() === label) {
              direction.value = option.value;
            }
          });
        }
      }
    }
    requestDialog.showModal();
    body.classList.add("no-scroll");
    const first = requestDialog.querySelector("input[name='name']");
    setTimeout(() => first && first.focus(), 120);
  };

  document.querySelectorAll("[data-open-request]").forEach((button) => {
    button.addEventListener("click", () => openRequest(button));
  });

  const closeRequest = () => {
    if (!requestDialog || !requestDialog.open) return;
    requestDialog.close();
    body.classList.remove("no-scroll");
  };

  if (requestDialog) {
    requestDialog.querySelectorAll("[data-close-dialog]").forEach((button) => {
      button.addEventListener("click", closeRequest);
    });

    requestDialog.addEventListener("click", (event) => {
      if (event.target === requestDialog) closeRequest();
    });

    requestDialog.addEventListener("close", () => {
      body.classList.remove("no-scroll");
    });
  }

  if (requestForm) {
    requestForm.addEventListener("submit", (event) => {
      event.preventDefault();
      if (!requestForm.reportValidity()) return;

      const data = new FormData(requestForm);
      const name = String(data.get("name") || "").trim();
      const company = String(data.get("company") || "").trim();
      const phone = String(data.get("phone") || "").trim();
      const direction = String(data.get("direction") || "").trim();
      const comment = String(data.get("comment") || "").trim();

      const message = [
        "Заявка с сайта БРИЗ",
        "Имя: " + name,
        company ? "Компания: " + company : "",
        "Телефон: " + phone,
        direction ? "Что интересует: " + direction : "",
        comment ? "Комментарий: " + comment : "",
      ]
        .filter(Boolean)
        .join("\n");

      if (successText) successText.textContent = message;
      if (requestMailto) {
        requestMailto.href = "mailto:brizpak@list.ru?subject=" + encodeURIComponent("Заявка с сайта БРИЗ") + "&body=" + encodeURIComponent(message);
      }

      if (successPanel) successPanel.classList.add("is-visible");
      requestForm.hidden = true;
      if (successPanel) successPanel.scrollIntoView({ block: "nearest", behavior: "smooth" });
    });
  }

  /* ---------- Lightbox ---------- */
  const galleryButtons = Array.from(document.querySelectorAll("[data-lightbox]"));
  if (galleryButtons.length) {
    const lightbox = document.createElement("dialog");
    lightbox.className = "lightbox";
    lightbox.innerHTML = `
      <div class="lightbox__inner">
        <button class="lightbox__close" type="button" aria-label="Закрыть галерею">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19"/></svg>
        </button>
        <button class="lightbox__nav lightbox__nav--prev" type="button" aria-label="Предыдущее фото">←</button>
        <img class="lightbox__img" src="" alt="">
        <button class="lightbox__nav lightbox__nav--next" type="button" aria-label="Следующее фото">→</button>
        <p class="lightbox__caption"></p>
      </div>`;
    document.body.appendChild(lightbox);

    const lightboxImg = lightbox.querySelector(".lightbox__img");
    const lightboxCaption = lightbox.querySelector(".lightbox__caption");
    let currentIndex = 0;

    const showImage = (index) => {
      currentIndex = (index + galleryButtons.length) % galleryButtons.length;
      const button = galleryButtons[currentIndex];
      const full = button.getAttribute("data-full");
      const alt = button.querySelector("img") ? button.querySelector("img").alt : "";
      const caption = button.getAttribute("data-caption") || "";
      lightboxImg.src = full || "";
      lightboxImg.alt = alt;
      lightboxCaption.textContent = caption;
    };

    galleryButtons.forEach((button, index) => {
      button.addEventListener("click", () => {
        showImage(index);
        lightbox.showModal();
        body.classList.add("no-scroll");
      });
    });

    lightbox.querySelector(".lightbox__close").addEventListener("click", () => {
      lightbox.close();
    });

    lightbox.querySelector(".lightbox__nav--prev").addEventListener("click", () => {
      showImage(currentIndex - 1);
    });

    lightbox.querySelector(".lightbox__nav--next").addEventListener("click", () => {
      showImage(currentIndex + 1);
    });

    lightbox.addEventListener("click", (event) => {
      if (event.target === lightbox) lightbox.close();
    });

    lightbox.addEventListener("keydown", (event) => {
      if (event.key === "ArrowLeft") showImage(currentIndex - 1);
      if (event.key === "ArrowRight") showImage(currentIndex + 1);
    });

    lightbox.addEventListener("close", () => {
      body.classList.remove("no-scroll");
      lightboxImg.src = "";
    });
  }

  /* ---------- Scroll spy for side nav ---------- */
  const sideLinks = Array.from(document.querySelectorAll(".side-nav a[href^='#']"));
  if (sideLinks.length && "IntersectionObserver" in window) {
    const targets = sideLinks
      .map((link) => {
        const id = link.getAttribute("href");
        return id && id.length > 1 ? document.querySelector(id) : null;
      })
      .filter(Boolean);

    const spy = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (!entry.isIntersecting) return;
          sideLinks.forEach((link) => {
            link.classList.toggle("is-active", link.getAttribute("href") === "#" + entry.target.id);
          });
        });
      },
      { rootMargin: "-18% 0px -66% 0px", threshold: 0 }
    );

    targets.forEach((target) => spy.observe(target));
  }

  /* ---------- Current year ---------- */
  document.querySelectorAll("[data-year]").forEach((el) => {
    el.textContent = new Date().getFullYear();
  });
})();
