const sections = document.querySelectorAll('.section, .section-band');

// Opt into the fade from here rather than from the stylesheet, so a page whose
// script never runs shows its content instead of nothing.
document.documentElement.classList.add('js-reveal');

/**
 * Shows everything if the reveal has not started shortly after load.
 *
 * A hidden document reports no intersections at all — a background tab, a
 * thumbnail capture, a print of a page that was never scrolled — and the page
 * would sit at opacity 0 with nothing on screen. The animation is a nicety;
 * being readable is not.
 */
const giveUp = window.setTimeout(() => {
  document.documentElement.classList.remove('js-reveal');
}, 1200);

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        window.clearTimeout(giveUp);
        entry.target.classList.add('is-visible');
      }
    });
  },
  {
    threshold: 0.12,
  },
);

sections.forEach((section) => observer.observe(section));
