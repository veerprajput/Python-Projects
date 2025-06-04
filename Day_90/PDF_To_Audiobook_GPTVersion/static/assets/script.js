window.addEventListener('pdfLoaded', function() {
    // Signal that the PDF has finished rendering
    document.getElementById('play-btn').disabled = false;
    document.getElementById('pause-btn').disabled = false;
  });
  