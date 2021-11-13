$(document).ready(function() {
  setTimeout(function() {
    $(".alert").alert('close');
  }, 3000);
});

function tabToRound(event, round) {
  tabcontent = document.getElementsByClassName("tabcontent");
  for (var i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }

  tablinks = document.getElementsByClassName("tablinks");
  for (var i = 0; i < tablinks.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" active", "");
  }

  document.getElementById(round).style.display = "block";
  event.currentTarget.className += " active";
}
