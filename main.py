#%%
from retrieveData import retrieveData
from dates import nrOfDates


def main():
    # Retrieve data from retrieveData file
    data, filesNames = retrieveData()

    # Call dates function
    nrOfDates(data, filesNames)


if __name__ == "__main__":
    main()
# %%
