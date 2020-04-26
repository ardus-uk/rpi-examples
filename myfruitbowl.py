#!/usr/bin/python3

from FruitBowl import FruitBowl

fb = FruitBowl()
fb.show_contents()
fb.add_single("orange")
fb.show_contents()
fb.add_single("banana")
fb.show_contents()
fb.add_multiple("lemon",4)
fb.show_contents()
fb.add_multiple("grape", 300)
fb.show_contents()
fb.take_item("lemon")
fb.show_contents()
fb.take_item("orange")
fb.show_contents()
fb.take_item("orange")
fb.show_contents()
fb.add_single("python")
fb.show_contents()
fb.add_single("python")
fb.show_contents()