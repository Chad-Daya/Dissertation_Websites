$(window).ready(function (){
  
  var init = function(){
	popup();
	readProductData();
  };
  
  var isDone = true;
  
	var popup = function(){
		var $items = $('.mini-carousel ul');
		var $linkClick = $('.mini-carousel ul li a');
		$('.video-player').hide();
		$('.btn-view').on('click', function(){
			$('#quick-view-pop-up').fadeToggle();
			$('#quick-view-pop-up').css({"top":"34px", "left":"314px"});
			$('.mask').fadeToggle();
		});
		$('.mask').on('click', function(){
			$('.mask').fadeOut();
			$('#quick-view-pop-up').fadeOut();
		});

		//Quick View Close function
		$('.quick-view-close').on('click', function(){
			$('.mask').fadeOut();
			$('#quick-view-pop-up').fadeOut();
		});
    
		$('.prev').on('click', function(){
      			//animate on UL element of small image on the left
      		if(!isDone) return;
			if($items.position().top === 0){
				$items.css({'top':'-125px'});
				$items.children('li').last().prependTo($items);
			}
      		isDone = false;
			$('.mini-carousel ul').animate({
				top: "+=125px"
			}, 200 ,  function(){
          		isDone = true;
        	});
        	$('.image-large ul li').last().prependTo($('.image-large ul'));
		});

		$('.next').on('click', function(){
				//animate on UL element of class 'mini-carousel'
			if(!isDone) return;
			
      		if($items.position().top === 0){
        		$items.css({'top': '125px'});
				$items.children('li').first().appendTo($items);
        	}      		
      		isDone = false;
      		$('.mini-carousel ul').animate({
				top: "-=125px"
			}, 300 ,  function(){
        		isDone = true;
        	});	
			$('.image-large ul li').first().appendTo($('.image-large ul'));
		});
		$('.quick-view-video').on('click', function(){
			$('.video-player').toggle();
			$('.image-large ul').toggle();
		});
	};
	var readProductData = function(){
		$.getJSON("winners.json", function(result){
			$.each(result, function(val){
				console.log(val.key);
			});
		});
	};
	init();
});

//Script modified from Bootmd Quicview template