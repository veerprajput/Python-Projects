const audio = new Audio();
audio.src = "{{ url_for('static', filename='audio.mp3') }}";
audio.volume = 0.5;

document.getElementById('play-btn').addEventListener('click', function() {
  audio.play();
});

document.getElementById('pause-btn').addEventListener('click', function() {
  audio.pause();
});

document.getElementById('volume-slider').addEventListener('input', function() {
  audio.volume = this.value;
});
