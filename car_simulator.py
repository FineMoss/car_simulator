import Model   as M
import View    as V
import Control as C


def main():

    # initialize the app
    simulator = M.CarSimulator()
    view = V.View()
    control = C.Control(simulator, view)

    # run the app
    control.run()


if __name__ == '__main__':
    main()
else:
    print("WARNING: car_simulator.py is not running as "'__main__'" ")


