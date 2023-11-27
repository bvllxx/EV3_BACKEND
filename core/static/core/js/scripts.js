document.addEventListener("DOMContentLoaded", function() {
    const navbarLinks = document.querySelectorAll("#navbar a");

    navbarLinks.forEach(function(link) {
      if (link.href === window.location.href) {
        link.classList.add("active");
      }
    });
});