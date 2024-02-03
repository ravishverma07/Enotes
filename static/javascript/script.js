function scrollSkills(direction) {
    const skillBar = document.getElementById('skill-bar');
    const scrollAmount = 200;
    if (direction === 'left') {
      skillBar.scrollTo({
        left: skillBar.scrollLeft - scrollAmount,
        behavior: 'smooth'
      });
    } else if (direction === 'right') {
      skillBar.scrollTo({
        left: skillBar.scrollLeft + scrollAmount,
        behavior: 'smooth'
      });
    }
  }
  // JavaScript to hide the loading indicator when content is loaded
window.addEventListener('load', function() {
    const loadingOverlay = document.getElementById('loading-overlay');
    loadingOverlay.style.display = 'none';
    behavior: 'smooth'

  });
  