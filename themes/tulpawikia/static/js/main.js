function simplify(text) {
	text = text.toLowerCase();
	text = text.replace(/[^ 0-9A-Za-z\u0400-\u04FF]/g, " ");
	text = text.replace(/\s+/g, ' ');
	text = text.trim();
	return text;
}

var sitemap;
var oReq = new XMLHttpRequest();
oReq.open("GET", "/sitemap.gz", true);
oReq.responseType = "arraybuffer";
oReq.onload = function(oEvent) {
	var arrayBuffer = oReq.response;
	sitemap = JSON.parse(pako.inflate(arrayBuffer, {to: 'string'}));

	var query = decodeURI(location.hash);
	if (query[1] == '@') {
		var val = query.substring(2);
		$('.search-container').fadeToggle(80);
		$('#search-input').val(val);
		val = simplify(val);
		if (val != '') {
			$("#copy-search-query-btn").removeClass("hidden");
		}
		showResults(val);
		$('#search-input').focus();
		hadUrlQuery = true;
	}
};
oReq.send();

function addResult(item, text) {
	if (simplify(item['title']).indexOf(text) >= 0 || item['text'].indexOf(text) >= 0) {
		$(".results").append('<a class="item" href="'+item['url']+'""><p class="title">'+item['title']+'</p><div class="category">'+item['category']+'</div></a>');
		return true;
	}
	return false;
}
function showResults(text) {
	$(".results").empty();
	var totalResults = 0;
	if (sitemap) {
		for (var i = 0; i < sitemap['pages'].length; i++){
			if (addResult(sitemap['pages'][i], text))
				totalResults++;

			if (totalResults > 21)
				return;
		}
	}
}
function copyToClipboard(text) {
	if (window.clipboardData && window.clipboardData.setData) {
		return clipboardData.setData("Text", text); 

	} else if (document.queryCommandSupported && document.queryCommandSupported("copy")) {
		var ta = document.createElement("textarea");
		ta.textContent = text;
		ta.style.position = "fixed";
		document.body.appendChild(ta);
		ta.select();
		try {
			return document.execCommand("copy");
		} catch (ex) {
			return false;
		} finally {
			document.body.removeChild(ta);
		}
	}
}

$('#search-input').on('input', function() {
	$(".results").empty();
	var val = simplify($('#search-input').val());
	if (val != '') {
		$('#copy-search-query-btn').attr("data-title", "Копировать ссылку");
		$("#copy-search-query-btn").removeClass("hidden");
	} else {
		$("#copy-search-query-btn").addClass("hidden");
	}
	showResults(val);
});
$('#copy-search-query-btn').click(function() {
	$('#search-input').focus();
	var val = $('#search-input').val();
	var copied = copyToClipboard(window.location.origin + "/categories#@" + val);
	if (copied) {
		$('#copy-search-query-btn').attr("data-title", "Скопировано!");
	}
});

$('#search').click(function() {
	$('.search-container').fadeToggle(80);
	$('#search-input').val('');
	showResults('');
	$('#search-input').focus();
	$("#copy-search-query-btn").addClass("hidden");
});
$('.search-container').mousedown(function(e) {
	if ($('.overlay-content').find(e.target).length > 0)
		return;
	$('.search-container').fadeOut(80);
	$("#copy-search-query-btn").addClass("hidden");
});
$(document).keyup(function(e) {
	if (e.keyCode === 27) {
		$('.search-container').fadeOut(80);
		$("#copy-search-query-btn").addClass("hidden");
	}
});