//
//  UserPaletteData.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-29.
//

import Foundation
import SwiftUI

class UserPaletteData: ObservableObject {
    @Published var userPalettes: [String: String] = [:] // Dictionary with color names and hex codes

    init() {
        loadUserPalettes()
    }

    func loadUserPalettes() {
        if let palettes = UserDefaults.standard.dictionary(forKey: UserPaletteConstants.userPalettesKey) as? [String: String] {
            userPalettes = palettes
        }
    }

    func saveUserPalette(name: String, hexCode: String) {
        userPalettes[name] = hexCode
        UserDefaults.standard.set(userPalettes, forKey: UserPaletteConstants.userPalettesKey)
    }

    func deleteUserPalette(name: String) {
        userPalettes.removeValue(forKey: name)
        UserDefaults.standard.set(userPalettes, forKey: UserPaletteConstants.userPalettesKey)
    }

    func clearAllPalettes() {
        userPalettes.removeAll()
        UserDefaults.standard.removeObject(forKey: UserPaletteConstants.userPalettesKey)
    }
}


