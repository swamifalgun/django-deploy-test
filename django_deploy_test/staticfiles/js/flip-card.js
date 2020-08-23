// function flip() {
// 	$('.flip-card').toggleClass('flipped');
// }

function flip(cardname) {
    $(cardname).toggleClass('flipped');
}

$("button").click(function(){
	$("button").css("outline", "none");
});