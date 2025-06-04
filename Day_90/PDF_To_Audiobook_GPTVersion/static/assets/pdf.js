const filename = document.getElementById('filename').textContent;
const url = `{{ url_for('static', filename='${filename}') }}`;
pdfjsLib.getDocument(url).promise.then(function(pdf) {
  // Set up the PDF viewer
  const container = document.getElementById('pdf-container');
  for (let i = 1; i <= pdf.numPages; i++) {
    pdf.getPage(i).then(function(page) {
      const canvas = document.createElement('canvas');
      container.appendChild(canvas);
      const viewport = page.getViewport({ scale: 1 });
      canvas.width = viewport.width;
      canvas.height = viewport.height;
      const ctx = canvas.getContext('2d');
      const renderTask = page.render({ canvasContext: ctx, viewport: viewport });
      renderTask.promise.then(function() {
        if (i === pdf.numPages) {
          // Signal that the PDF has finished rendering
          window.dispatchEvent(new CustomEvent('pdfLoaded'));
        }
      });
    });
  }
});
