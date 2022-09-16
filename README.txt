Implements MVC architecture. The Model and the View are completely independent classes. Neither has any reference to the other.

I tried to preserve the structure of the original assignment, but made a few changes. The CarSimulator class was moved to Model.py, data initializion of CarSimulator was moved to Control.py, and I added defaults to the CarSimulator constructor. 


Running the App:
	- requires pygame and NumPy (both can be installed with pip)
	- run from inside the car_simulation folder to avoid 'FileNotFoundError' for car.png
	- run car_simulation.py


Controls:

	W key 
		- increases acceleration by 10 for 1 epoch 
		- if dt = 0.1 then velocity increases by 1 for each key press
	S key 
		- decreases acceleration by 10 for 1 epoch 
		- if dt = 0.1 then velocity decreases by 1 for each key press
	A key 
		- increases wheel_angle by .1 for 1 epoch
	D key 
		- decreases wheel_angle by .1 for 1 epoch
	ESC key 
		- quit the program
	MOUSE press 
		- resets the data model to 0
		- positions car at location of mouse click


Areas for improvement:

Pygame View:
	- draw the car based on wheelbase instead of from center
	- implement sprites with collision detection
	- introduce more game assets, e.g. boulder that stops the car on collision 
	- improve car control:
		- use constant wheel_angle while A or D is pressed
		- use constant acceleration while W or S is pressed
		- use dynamic acceleration 
		- implement car braking

Physics Model:
	- use pygame math instead of NumPy in Model.py (reduce dependencies)
	- implement constraints for the car, e.g. max velocity, min/max wheel_angle, etc.
	- use resistance to decrease velocity over time while no input is given

Multithreading: 
	- while waiting for the next frame, we could be computing the simulationStep




