const sections = document.querySelectorAll('.section, .section-band');

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
      }
    });
  },
  {
    threshold: 0.12,
  },
);

sections.forEach((section) => observer.observe(section));
