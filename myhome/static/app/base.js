$('.left.demo.sidebar').first()
  .sidebar('attach events', '.open.item', 'show')
	.sidebar('setting', 'transition', 'overlay')
;

$('.open.item')
  .removeClass('disabled')
;

$('.ui.search')
  .search({
		minCharacters : 3
  })
;

$('.message .close')
  .on('click', function() {
    $(this)
      .closest('.message')
      .transition('fade')
    ;
  })
;