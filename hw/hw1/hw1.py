#homework1 for cit590 by changan 8/31/2017;
#copyright reserved by Quankang Wang, UID:54162826.
#I have done it on my own.
#python gramma is strange, man.


def clear():
	#enable the game part but still in the loop.
	global time,altitude,velocity,fuel,fuel_consume,gameloop;
	gameloop=1;
	time = 0;
	altitude = 1000.0;#m
	velocity = 100.0 ;# m/s
	fuel = 1000.0;#unit
	fuel_consume= 0;

def game_juge():
	#safe conditon check, if landing jump out of the game stay in the loop.
	global gameloop;
	if altitude <= 0.0 :
		if velocity <= 10.0 :
			print("\n safe landing.")
			print("\n your landing parameter is : \n time :%d \n velocity :%f \n fuel left:%f" %(time,velocity,fuel));
			gameloop=0;
			return;
		else:
			print("\n you crashed.")
			print("\n your landing parameter is : \n time :%d \n velocity :%f \n fuel left:%f" %(time,velocity,fuel));
			gameloop=0;
			return;

def game_play():
	#game play
	global time,altitude,velocity,fuel,fuel_consume;
	print("\n your current parameter is : \n time :%d \n velocity :%f \n altitude: %f \n fuel:%f" %(time,velocity,altitude,fuel));
	fuel_consume=float(input("\n input the fuel you want to consume (from 0 to 1000)"));
	#if fuel_consume is negative, see it as zero;
	if fuel_consume<0:
		fuel_consume=0;
	#if fuel_consume surpass the remain fuel, see it consuming it all.
	if fuel_consume > fuel:
		print("\n not enough fuel;")
		fuel_consume = fuel;
	#every second the fuel consume, the altitude descend , velocity ascends, time flows, this is life man.
	fuel -= fuel_consume;
	velocity -= fuel_consume*0.15;
	altitude -= velocity;
	time += 1;
	velocity += 1.6;

#inital the loop and gameloop for it to start.
global loop;
global gameloop;
loop =1;
gameloop=1;
while loop == 1:
	#clear the inital terms every time the game started, todo: flexible initals by inputing.
	clear();
	while gameloop==1:
		game_play();
		game_juge();
	again=0;
	again = float(input("\n if continue input 1, if not press anybutton else."));
	if again == 1:
		continue;
	else:
		print("\n game is ended.")
		break;