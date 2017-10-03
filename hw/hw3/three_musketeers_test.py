#Quankang Wang,CIT590 HW3
#finished all by myself
#UID:54162826.

import unittest
from three_musketeers import *

left = 'left'
right = 'right'
up = 'up'
down = 'down'
M = 'M'
R = 'R'
_ = '-'

class TestThreeMusketeers(unittest.TestCase):

    def setUp(self):
        set_board([ [_, _, _, M, _],
                    [_, _, R, M, _],
                    [_, R, M, R, _],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ])

    def test_create_board(self):
        create_board()
        self.assertEqual(at((0, 0)), 'R')
        self.assertEqual(at((0, 4)), 'M')

    def test_set_board(self):
        self.assertEqual(at((0, 0)), '-')
        self.assertEqual(at((1, 2)), 'R')
        self.assertEqual(at((1, 3)), 'M')

    def test_get_board(self):
        self.assertEqual([ [_, _, _, M, _],
                           [_, _, R, M, _],
                           [_, R, M, R, _],
                           [_, R, _, _, _],
                           [_, _, _, R, _] ],
                         get_board())

    def test_string_to_location(self):
        #self.fail() # Replace with tests
        self.assertEqual(string_to_location('B4'),(1,3))

    def test_location_to_string(self):
        #self.fail() # Replace with tests
        self.assertEqual(location_to_string((2,3)),'C4')

    def test_at(self):
        board = [ [_, _, _, M, _],[_, _, R, M, _],[_, R, M, R, _],[_, R, _, _, _],[_, _, _, R, _] ]
        #self.fail() # Replace with tests
        self.assertEqual(at((0,4)),board[0][4])
       
    def test_all_locations(self):
        #self.fail() # Replace with tests
        self.assertEqual(all_locations(),[(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4),(2,0),(2,1),(2,2),(2,3),(2,4),(3,0),(3,1),(3,2),(3,3),(3,4),(4,0),(4,1),(4,2),(4,3),(4,4)])

    def test_adjacent_location(self):
        self.assertEqual(adjacent_location((1,3),"up"),(0,3)) # Replace with tests
        
    def test_is_legal_move_by_musketeer(self):
        self.assertTrue(is_legal_move_by_musketeer((1,3),left))
        self.assertFalse(is_legal_move_by_musketeer((1,3),right))
        #self.fail() # Replace with tests
        
    def test_is_legal_move_by_enemy(self):
        self.assertTrue(is_legal_move_by_enemy((1,2),up))
        self.assertFalse(is_legal_move_by_enemy((1,2),right))
        #self.fail() # Replace with tests

    def test_is_legal_move(self):
        self.assertTrue(is_legal_move((1,3),left))
        self.assertFalse(is_legal_move((0,3),up))
        #self.fail() # Replace with tests
        
    def test_has_some_legal_move_somewhere(self):
        set_board([ [_, _, _, M, _],
                    [_, R, _, M, _],
                    [_, _, M, _, R],
                    [_, R, _, _, _],
                    [_, _, _, R, _] ] )
        self.assertFalse(has_some_legal_move_somewhere('M'))
        self.assertTrue(has_some_legal_move_somewhere('R'))
        #self.fail() # Put additional tests here

    def test_possible_moves_from(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, _],
                    [_, _, M, _, _],
                    [_, R, R, _, _],
                    [_, _, _, R, _] ] )
        self.assertEqual(possible_moves_from((0,3)),['right'])
        self.assertEqual(possible_moves_from((2,2)),['down'])
        self.assertEqual(possible_moves_from((0,4)),['down'])

        #self.fail() # Replace with tests

    def test_can_move_piece_at(self):
        set_board([ [_, _, _, M, R],
                    [_, _, _, M, M],
                    [_, _, R, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertFalse(can_move_piece_at((0,4)))   
        self.assertTrue(can_move_piece_at((1,4)))
        #self.fail() # Replace with tests

    def test_is_legal_location(self):
        self.assertTrue(is_legal_location((4,0)))
        self.assertFalse(is_legal_location((0,10)))
        self.assertFalse(is_legal_location((-1,5)))
        #self.fail() # Replace with tests

    def test_is_within_board(self):
        self.assertTrue(is_within_board((0,4),left))
        self.assertFalse(is_within_board((0,4),up))
        #self.fail() # Replace with tests

    def test_all_possible_moves_for(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertEqual(all_possible_moves_for('R'),[((0,2),left),((0,2),down)])
        self.assertListEqual(all_possible_moves_for('M'),[((0,3),left),((0,3),right),((1,4),up)])
        #self.fail() # Replace with tests
        
    def test_make_move(self):
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, M],
                    [_, _, _, _, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        make_move((0,3),left)
        self.assertEqual(at((0,2)),M)
        self.assertEqual(at((0,3)),_)
        make_move((1,4),up)
        self.assertEqual(at((0,4)),M)
        self.assertEqual(at((1,4)),_)        
        #self.fail() # Replace with tests
        
    def test_value(self):
        self.assertEqual(value((1,3),3,3),(2,0))

    def test_choose_computer_move(self):
        self.assertTrue(choose_computer_move('M') in all_possible_moves_for('M'))
        self.assertTrue(choose_computer_move('R') in all_possible_moves_for('R'))
        #self.fail() # Replace with tests; should work for both 'M' and 'R'

    def test_m_position(self):
        self.assertEqual(m_position(),[(0,3),(1,3),(2,2)])

    def test_samerow(self):
        self.assertTrue(samerow((1,4),(1,3)))
        self.assertFalse(samerow((1,4),(2,3)))

    def test_is_enemy_win(self):
        set_board([ [_, _, _, _, M],
                    [_, _, R, _, _],
                    [_, R, _, R, _],
                    [_, R, _, _, _],
                    [M, _, _, _, M] ])
        self.assertFalse(is_enemy_win())
        set_board([ [_, _, R, M, R],
                    [_, _, _, M, _],
                    [_, _, _, M, _],
                    [_, _, _, _, _],
                    [_, _, _, _, _] ] )
        self.assertTrue(is_enemy_win())
        #self.fail() # Replace with tests

unittest.main()
