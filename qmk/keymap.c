/* Copyright 2019
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 2 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include QMK_KEYBOARD_H

enum layers {
  _BASE = 0,
  _FN1,
};

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    
    [_BASE] = LAYOUT_ortho_4x4(A(KC_TAB),  S(A(KC_TAB)), A(KC_F13),  A(KC_F4), \
                               KC_F13,     KC_F14,       KC_F15,     KC_F16,   \
                               KC_F17,     KC_F18,       KC_F19,     KC_F20,   \
                               KC_F21,     KC_F22,       KC_F23,     KC_F24), \

    [_FN1] = LAYOUT_ortho_4x4(RGB_TOG,  RGB_HUI,  RGB_SAI,  RGB_VAI, \
                              RGB_MOD,  RGB_HUD,  RGB_SAD,  RGB_VAD, \
                              _______,  _______,  _______,  RESET,   \
                              BL_STEP,  _______,  _______,  _______)
};

bool process_record_user(uint16_t keycode, keyrecord_t *record)
{
  return true;
}
