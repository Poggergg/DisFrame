import os

class MD:
  @staticmethod
  def read():
    with open("readme.md", "r") as E:
      return E.readlines()
  
  @staticmethod
  def write(content):
    the = MD.read()
    with open("readme.md", "w") as E:
      E.write(f"{the}\n{content}")

MD.write(content="hi")