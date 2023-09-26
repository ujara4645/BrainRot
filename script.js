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
  $("#slider").slider({
    create: function() {
      $("#custom-handle").text($(this).slider("value"));
    },
    slide: function(event, ui) {
      $("#custom-handle").text(ui.value);
    }
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
    const minimumPrice = $("#slider").slider("value");
    const gameDescription = $("#gameDescription").val();
    
    // ... Perform further actions such as sending the data to the server ...
  });
});
