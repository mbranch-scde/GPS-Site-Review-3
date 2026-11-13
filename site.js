/* Small behaviors: district access form, library filter, in-site guide viewer. */
(function () {
  const $ = (s, r = document) => r.querySelector(s);

  // ---- District access form: opens a mailto to that district's user admin(s)
  const form = $("[data-access]");
  if (form) {
    const data = JSON.parse($("#districts").textContent);
    const sel = $("#district"), btn = $("#district-btn"), to = $("#district-to");
    Object.keys(data).sort().forEach(d => sel.add(new Option(d, d)));
    sel.addEventListener("change", () => {
      const admins = data[sel.value] || [];
      if (!admins.length) {
        btn.classList.add("disabled"); btn.setAttribute("aria-disabled", "true");
        btn.setAttribute("href", "#access"); to.textContent = ""; return;
      }
      const addr = admins.map(a => a.email).join(",");
      const q = "subject=" + encodeURIComponent(form.dataset.subject) + "&body=" + encodeURIComponent(form.dataset.body);
      btn.href = "mailto:" + addr + "?" + q;
      btn.classList.remove("disabled"); btn.removeAttribute("aria-disabled");
      to.textContent = "Your email will go to: " + admins.map(a => a.name).join(" and ");
    });
    btn.addEventListener("click", e => { if (btn.classList.contains("disabled")) e.preventDefault(); });
  }

  // ---- Library: topic rail, search, Navigator and Format filters (mirrors the original hub)
  const lib = $("#lib");
  if (lib) {
    const q = $("#q"), nav = $("#f-nav"), fmt = $("#f-format"), empty = $("#empty"), countEl = $("#count");
    const cards = [...lib.querySelectorAll(".resource-card")];
    const total = +lib.dataset.total;
    let topic = new URLSearchParams(location.search).get("topic") || "";
    const apply = () => {
      const s = q.value.trim().toLowerCase();
      let n = 0;
      cards.forEach(c => {
        const show = (!topic || c.dataset.topic === topic) && (!nav.value || c.dataset.nav === nav.value) &&
                     (!fmt.value || c.dataset.format === fmt.value) && c.dataset.text.includes(s);
        c.style.display = show ? "" : "none";
        if (show) n++;
      });
      countEl.textContent = lib.dataset.count.replace("{shown}", n).replace("{total}", total);
      empty.style.display = n ? "none" : "block";
      document.querySelectorAll(".topic-button").forEach(b => b.setAttribute("aria-pressed", b.dataset.topic === topic));
    };
    document.querySelectorAll(".topic-button").forEach(b => b.addEventListener("click", () => { topic = b.dataset.topic; apply(); }));
    [q, nav, fmt].forEach(el => el.addEventListener("input", apply));
    $("#f-reset").addEventListener("click", () => { q.value = ""; nav.value = ""; fmt.value = ""; topic = ""; apply(); });
    apply();
  }

  // ---- Guide viewer: keeps every guide inside the site, with a way back
  const frame = $("#v-frame");
  if (frame) {
    const cat = JSON.parse($("#catalog").textContent), labels = JSON.parse($("#type-labels").textContent);
    const params = new URLSearchParams(location.search);
    const slug = params.get("g");
    const g = Object.prototype.hasOwnProperty.call(cat, slug) ? cat[slug] : null;   // only known guides can load
    if (!g) {
      frame.style.display = "none"; $(".viewer-bar").style.display = "none"; $("#v-missing").style.display = "block";
    } else {
      let t = params.get("t");
      if (!g.types.includes(t)) t = g.types[0];
      const src = "guides/" + slug + "/" + t + ".html";
      frame.src = src;
      $("#v-title").textContent = g.title;
      $("#v-new").href = src;
      document.title = g.title + " | GPS Navigator Hub";
      const sw = $("#v-switch");
      if (g.types.length > 1) {
        g.types.forEach(k => {
          const a = document.createElement("a");
          a.href = "viewer.html?g=" + slug + "&t=" + k; a.textContent = labels[k] || k;
          if (k === t) a.setAttribute("aria-current", "true");
          sw.appendChild(a);
        });
      }
    }
  }
})();
