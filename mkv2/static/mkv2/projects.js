$(document).ready(function () {
	// Reset scroll position
	$(this).scrollTop(0);

	// Render image galleries 
	$('.slick-carousel').slick({
		infinite:true,
		centerMode: true,
		variableWidth: true,
		arrows: false,
		dots: false,
		speed: 500,
		cssEase: 'linear',
		useTransform:false,
    autoplay: true
//      autoplaySpeed: 6000,
	});


	$('#filter-search').keyup(function(event){ 
		searchFilters(event)
	})
	$('#clearSelectionButton').click(function(event){ uncheckAll(event) })
	$('#clearFiltersSearchButton').click(function(event){ 
		uncheckAll(event)
		$('#searchBarButton').click()
	 })

	const logo = document.querySelector("#logo");
	const header = document.querySelector(".projectsHeading");
	
	const tl = new TimelineMax(); 

	// ----------------- PROJECTS ANIMATION -----------------

	tl.fromTo(logo,.25,{x: 200, opacity: 0},{x:-10, opacity: .8});
    tl.fromTo(logo,.25,{x: -20, opacity: .8},{x:0, opacity: 1});
    tl.fromTo(header,.8,{x: 50, opacity: 0},{x:0, opacity: 1});

    $('#items').on('click', function(event) { 
		if (this.hash !== "") {
		//   event.preventDefault();
		  var hash = this.hash;

		  $('html, body').animate({
		    scrollTop: $('#items').offset().top
		  }, 700);
		}
	});

	// Listeners
	// $('card').hover(
	// 	function(){
	// 		$(this).css('box-shadow', '1px 8px 20px grey');
	// 		$(this).css('-webkit-transition', 'box-shadow .375s ease-in-out');
	// 		// box-shadow: 1px 8px 20px grey;
    // 		// -webkit-transition: box-shadow .375s ease-in-out;
	// 	}, function() {
	// 		$(this).css('box-shadow', '0px');
	// 		$(this).css('-webkit-transition', 'box-shadow .375s ease-in-out');
	// });
});

//Function to update tag filters when searched 
function searchFilters(event) {
    event.preventDefault()

    var search = $('#filter-search')[0].value.split(' ')

    $("#filter-card .scroll-section label").each(function(){ 
        var filter = this.innerText.toUpperCase()
        var includesQuery = false

        for (i = 0; i < search.length; i++) {
            var query = search[i].toUpperCase()

            if (filter.includes(query)) {
                includesQuery = true
                break
            }
        }

        if(!includesQuery) { 
        	if(!$(this).find('input').is(':checked')) { $(this).hide() }
        } else { $(this).show() }
    })
}

// Uncheck all filters
function uncheckAll(event) {
    event.preventDefault()
    $("#filter-card .scroll-section input").prop("checked", false)
}