$(document).ready(function() {
  // Genres array
  const genres = [
    'Adventure', 'RPG', 'Puzzle', 'Brawler', 'Indie', 'Platform',
    'Turn Based Strategy', 'Simulator', 'Shooter', 'Strategy', 'Music', 
    'Arcade', 'Fighting', 'Visual Novel', 'Tactical', 'Card & Board Game',
    'Sport', 'Racing', 'MOBA', 'Point-and-Click', 'Real Time Strategy',
    'Quiz/Trivia', 'Pinball'
  ];

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

  function get_Checked_Values(checkboxName) {
    var checkboxes = document.getElementsByName(checkboxName);
    result = [];
    for (var i = 0; i < checkboxes.length; i++) {
      if (checkboxes[i].checked) {
        result.push(checkboxes[i].value);
      }
    }
    ret = "";
    if (result.length > 1) {
      for (var i = 0; i < result.length - 2; i++) {
        ret += result[i] + "+";
      }
      ret += result[result.length - 1];
    } else if (result.length == 1) {
      ret += result[0];
    }
    return ret;
  }

  // Form submission
  $("#gameRecommendationForm").submit(function(e) {
    e.preventDefault();

    const selectedGenres = get_Checked_Values('genre-cbx');
    const selectedPlats = get_Checked_Values('plat-cbx');
    const minimumRating = $("#slider").slider("value");
    const gameDescription = $("#gameDescription").val();

    // ... Perform further actions such as sending the data to the server ...
    document.getElementById("submit-button").onclick = function () {
      location.href = "/results?query=form&desc="+gameDescription+"&rating="+minimumRating+"&genres="+selectedGenres+"&platforms="+selectedPlats; //the page to redirect
    };
    document.getElementById("random-button").onclick = function () {
      location.href = "/results?query=random"; //the page to redirect
    };

  });
});