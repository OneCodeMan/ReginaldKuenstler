//
//  UserPaletteViewModel.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-22.
//

import Foundation

// MARK: User Palette VM
// fetch and delete

class UserPaletteViewModel: ObservableObject {
    
    @Published var userPaletteColours: [PaletteColour] = []
    @Published var filteredUserPaletteColours: [PaletteColour] = []
    
    // ["Red": [], "Green": [], "Blue": [], ...]
    @Published var groupedColours: [String: [PaletteColour]] = [:]
    
    @Published var isLoading: Bool = false
    
    init() {
        // UserDefaultsHelper.clearUserPaletteFromDefaults()
        self.fetchUserPalettes()
    }
    
    /**
     For now, in UserDefaults:
     userPalette = ["Cadmium Blue": "#223242"]
     */
    func fetchUserPalettes() {
        self.userPaletteColours = []
        let defaults = UserDefaults.standard
        
        if UserDefaultsHelper.isKeyPresentInUserDefaults(key: "userPalettes") {
            print("[--UserPaletteViewModel we have a palette, gonna retrieve them now...")
            if let userPaletteFromUserDefaults = defaults.dictionary(forKey: "userPalettes") as? [String: String]  {
                
                // take the user default palette and convert to PaletteColour objects
                for (name, hexCode) in userPaletteFromUserDefaults {
                    let generatedPaletteColour = PaletteColour(colourName: name, hexCode: hexCode, isUserOwned: true)
                    self.userPaletteColours.append(generatedPaletteColour)
                }
                
                self.filteredUserPaletteColours = self.userPaletteColours // TODO: DRY
                self.groupedColours = ColourHelper.groupColours(colours: self.filteredUserPaletteColours)
                // print("GROUPED COLOURS:\n\n \(self.groupedColours)\n\n")
            } else {
                // TODO: throw error
                fatalError("failed to retrieve colours from user defaults.")
            }
        } else {
            print("[--UserPaletteViewModel No user defaults initially, user must be on app for first time.")
//            let initialUserPalette: [String: String] = [:]
//            defaults.set(initialUserPalette, forKey: "userPalettes")
            
            // FOR TESTING
            let mockUserPalette: [String: String] = [:
//                "Viridian": "#40826D",
//                "Sienna": "#E97451",
//                "Cadmium Red": "#D22B2B",
//                "Red Ochre": "#913831",
//                "Burnt Umber": "#6E260E",
//                "Ultramarine": "#0437F2"
            ]
            
            // display
            let userPaletteColoursAsPalette = mockUserPalette.map { PaletteColour(colourName: $0.key, hexCode: $0.value) }
            self.userPaletteColours = userPaletteColoursAsPalette // TODO: sort alphabetically
            self.filteredUserPaletteColours = self.userPaletteColours // TODO: DRY
            
//            for colour in userPaletteColours {
//                let group = ColourHelper.groupColours(colours: userPaletteColours)
//                self.groupedColors[group]?.append(colour)
//            }
            
            // actually add them to user defaults
            defaults.set(mockUserPalette, forKey: "userPalettes")
        }
        
    }
    
    // MARK: Search functionality
    func filterPaletteColours(term: String) {
        isLoading = true
        self.filteredUserPaletteColours = self.userPaletteColours.filter{ $0.colourName.contains(term) }
        print("[--PaletteViewModel filtering paletteColours based on term: \(term). Contains \(self.filteredUserPaletteColours.count) items.\n \(self.userPaletteColours)")
        isLoading = false
    }
        
    func resetFilteredPaletteColours() {
        isLoading = true
        self.filteredUserPaletteColours = self.userPaletteColours
        isLoading = false
    }
}