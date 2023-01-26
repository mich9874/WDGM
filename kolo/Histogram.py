from BaseImage import *


class Histogram:
    """
    klasa reprezentujaca histogram danego obrazu
    """
    values: np.ndarray  # atrybut przechowujacy wartosci histogramu danego obrazu

    def __init__(self, values: np.ndarray=None) -> None:
        if values is None:
            self.values = []
        elif values.shape[-1] == 3:
            red = np.histogram(values[:,:,0], bins=256, range=(0,256))[0]
            green = np.histogram(values[:,:,1], bins=256, range=(0,256))[0]
            blue = np.histogram(values[:,:,2], bins=256, range=(0,256))[0]
            self.values = np.vstack([red,green,blue])
        else:
            self.values = np.histogram(values, bins=256, range=(0,256))[0]



    def plot(self) -> None:
        #metoda wyswietlajaca histogram na podstawie atrybutu values
        if len(self.values) == 3:
            kolorki = ["red", "green", "blue"]
            fig, ax = plt.subplots(1,3, figsize=(20,5))
            for i in range(3):
                histogram = self.values[i]
                bin_edges = np.array(range(256))
                ax[i].plot(bin_edges, histogram, color=kolorki[i])

                ax[i].set_title("Histogram")
                ax[i].set_xlabel("Wartości kolorów")
                ax[i].set_ylabel("Liczba pixeli")
        else:
            plt.figure()
            plt.title("Histogram szarości")
            plt.xlabel("Wartość szarosci")
            plt.ylabel("Liczba pixeli")
            plt.plot(self.values, color="black")

    def to_cumulated(self) -> 'Histogram':
        hist_cum = Histogram()
        if len(self.values) == 3:
            for i in self.values:
                hist_cum.values.append(np.cumsum(i))
        else:
            hist_cum.values = np.cumsum(self.values)
        return hist_cum