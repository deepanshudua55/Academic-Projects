// All global variables used in the program.

	var pongObj = null;
	var paddleObject = null;
	var ballXcoord = 0;
	var ballYcoord;
	var animateX=null ;
	var position = null;
	var animateY = null;
	var ballmove_countX=0;
	var ballmove_countY=0;
	var paddlemoveY = 0;
	var time = 80;
	var vel= 0;
	var counter = 0;
	
	
	
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
// setSpeed function sets the speed of the pong ball on the user input			
	function setSpeed(vel){
		if (vel == 0)
		{
			time = 80;
		}
		if (vel== 1)
		{
			time= 30;
		}
		if(vel == 2)
		{
			time = 18;
		}
		startGame();
	
	}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------				
	function init()
	{
		
		pongObj = document.getElementById('ball');
		paddleObject = document.getElementById("paddle");
		pongObj.style.position= 'relative'; 
		pongObj.style.left = '0px'; 
		pongObj.style.top = '-50px';
		ballYcoord = parseInt(pongObj.style.top);
	}
	
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------			
// startGame function starts the game on mouse click.
	function startGame()
	{
	clearTimeout(animateX);
	clearTimeout(animateY);
	animateX=setInterval(function(){moveballXcoord()},time);
	animateY=setInterval(function(){moveballYcoord()},time);
	
	}
	
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------		
//moveBallXcoord function moves the pong all the X axis i.e horizontally. 					
	function moveballXcoord()
	{

		if (parseInt(pongObj.style.left) == 0||ballmove_countX==0 )
			{
				pongObj.style.left = parseInt(pongObj.style.left) + 10 + 'px';
				ballmove_countX =0;
				
			}
		bottomPad = parseInt(paddleObject.style.top) - 95
		if (((parseInt(pongObj.style.left) == 1010 )&&(parseInt(paddleObject.style.top) + 45 > parseInt(pongObj.style.top)) && parseInt(pongObj.style.top) > bottomPad )|| ballmove_countX == 1)
		{
				
			pongObj.style.left = parseInt(pongObj.style.left) - 10 + 'px';
			ballmove_countX = 1;
			
		}
		if (parseInt(pongObj.style.left) == 1060){
			counter = counter + 1
			document.getElementById("message").innerHTML = counter;
			stop();
		}
	}			
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------		
//moveBallYcoord function moves the pong all the Y axis i.e vertically. 		
	function moveballYcoord()
	{
		if (parseInt(pongObj.style.top) == -50||ballmove_countY==0 )
			{
				pongObj.style.top= parseInt(pongObj.style.top) + 10 + 'px';
				ballmove_countY =0;
			}
		if ((parseInt(pongObj.style.top) == 500 )|| ballmove_countY == 1)
		{
			pongObj.style.top = parseInt(pongObj.style.top) - 10 + 'px';
			ballmove_countY = 1;
		}
	}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
// movePaddle function moves the paddle vertically
	function movePaddle()
	{
		
		Xmouse =  window.event.clientX ;
		Ymouse =  window.event.clientY ;
		s = "X: " + Xmouse + " " + "Y: " + Ymouse  
		if (Ymouse < 500){
			paddleObject.style.top= Ymouse;
		}
		
			
	} 
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
// stop function is used in stopping the game.					
	function stop(){
		clearTimeout(animateX);
		clearTimeout(animateY);
		pongObj.style.left = '0px'; 
		
	}
//-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------	
// resetCounter function resets the game.
	function resetCounter(){
		stop();
		counter = 0
		document.getElementById("message").innerHTML = counter;
	
	}
window.onload =init;