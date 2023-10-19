$(document).ready(function() {
  // Genres array
  const genres = [
    'Adventure', 'RPG', 'Puzzle', 'Brawler', 'Indie', 'Platform',
    'Turn Based Strategy', 'Simulator', 'Shooter', 'Strategy', 'Music', 
    'Arcade', 'Fighting', 'Visual Novel', 'Tactical', 'Card & Board Game',
    'Sport', 'Racing', 'MOBA', 'Point-and-Click', 'Real Time Strategy',
    'Quiz/Trivia', 'Pinball'
  ];

  // Generating buttons dynamically
  genres.forEach((genre) => {
      let button = $('<input/>', {
          type: 'button',
          class: 'btn btn-dark btn-lg col genre-button',
          value: genre
      });
      $('#genreSelection').append(button);
  });

  // Initializing jQuery UI slider
  var handle = $( "#custom-handle" );
  $("#slider").slider({
  create: function() {
      handle.text( $( this ).slider( "value" ) );
    },
    slide: function( event, ui ) {
      handle.text( ui.value );
    },
    max: 5,
    min: 0,
    step: 0.1,
  });

  // Highlighting the selected genre button
  $(".genre-button").on("click", function() {
    $(".genre-button").removeClass("btn-selected"); // Assuming btn-selected is a class that highlights the button
    $(this).addClass("btn-selected");
  });

  // Form submission
  $("#gameRecommendationForm").submit(function(e) {
    e.preventDefault();

    const selectedGenre = $(".btn-selected").val();
    const minimumRating = $("#slider").slider("value");
    const gameDescription = $("#gameDescription").val();

    // ... Perform further actions such as sending the data to the server ...
    document.getElementById("submit-button").onclick = function () {
      location.href = "http://localhost:8000/brain_rot/results?desc="+gameDescription+"&rating="+minimumRating; //the page to redirect
    };
    document.getElementById("random-button").onclick = function () {
      location.href = "http://localhost:8000/brain_rot/results"; //the page to redirect
    };

  });
});