from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from config import *


class Piece:
    classes = {
        "p": "pawn",
        "n": "knight",
        "b": "bishop",
        "r": "rook",
        "q": "queen",
        "k": "king"
    }

    colors = {
        "w": "white",
        "b": "black"
    }

    columns = ["a", "b", "c", "d", "e", "f", "g", "h"]

    def __init__(self, name, position):
        self.name = self.expand(*name)
        self.position = self.to_coordinate(position)

    def expand(self, color, class_):
        return self.colors[color] + " " + self.classes[class_]

    def to_coordinate(self, position):
        return self.columns[int(position[0]) - 1] + position[1]

    def __str__(self):
        return f"the {self.name} is at {self.position}"

    def __repr__(self):
        name = self.name.title().replace(" ", "")
        return f"{name}({self.position.title()})"


def create_browser():
    options = Options()
    PROFILE_PATH and options.add_argument(f"--user-data-dir={PROFILE_PATH}")
    PROFILE_NAME and options.add_argument(f"--profile-directory={PROFILE_NAME}")
    options.add_experimental_option("detach", DETACH)
    return webdriver.Chrome(options=options)


def open_chess(driver: WebDriver):
    driver.get("https://www.chess.com/play/computer")
    if first_div := driver.find_elements(By.CLASS_NAME, "modal-first-time-button"):
        first_div[0].find_element(By.TAG_NAME, "button").click()


def get_board(driver: WebDriver):
    raw_pieces = driver.find_elements(By.CLASS_NAME, "piece")
    pieces = [piece.get_attribute("class").split(" ")[1:] for piece in raw_pieces]
    board = []
    for piece, position in pieces:
        board.append(Piece(piece, position.split("-")[1]))
    return board
