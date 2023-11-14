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
    ret = "";
    for (var i = 0; i < checkboxes.length; i++) {
      if (checkboxes[i].checked) {
        // result.push(checkboxes[i].value);
        ret += checkboxes[i].value;
        if (i != checkboxes.length - 1) {
          ret += "+";
        }
      }
    }
    return ret;
  }

  function normal_results() {
    const selectedGenres = get_Checked_Values('genre-cbx');
    const selectedPlats = get_Checked_Values('plat-cbx');
    const minimumRating = $("#slider").slider("value");
    const gameDescription = $("#gameDescription").val();
    location.href = "/results?query=form&desc="+gameDescription+"&rating="+minimumRating+"&genres="+selectedGenres+"&platforms="+selectedPlats; //the page to redirect
  }

  function random_results() {
    location.href = "/results?query=random"; //the page to redirect
  } 

  // Form submission
  $("#gameRecommendationForm").submit(function(e) {
    e.preventDefault();
    normal_results();
  });
  $("#gameRecommendationForm2").submit(function(e) {
    e.preventDefault();
    random_results();
  });
});