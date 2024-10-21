//
//  UserPaletteViewModel.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import Foundation

// MARK: Create User Palette VM
// add to palette

class CreateUserPaletteViewModel: ObservableObject {
    // user can choose colours from map.
    @Published var paletteColours: [PaletteColourSelectItem] = []
    @Published var filteredPaletteColours: [PaletteColourSelectItem] = []
    @Published var isLoading: Bool = false
    
    init() {
        Task { try await self.fetchPaletteColours() }
    }
    
    @MainActor
    func fetchPaletteColours(completion: (([VColour]) -> Void)? = nil) async throws {
        let mapper = ColourMapper()
        
        mapper.createColourMapFromCSV { colourMap in
            
            // print("[--PaletteViewModel generateColourMapping() colourMap \(colourMap.count) items")
            
            // convert the colourMap ([VColour]) to an array of PaletteColours
            for vColour in colourMap {
                let generatedPaletteColour = PaletteColour(fromVColour: vColour)
                let paletteColourSelectItem = PaletteColourSelectItem(paletteColour: generatedPaletteColour, isSelected: false)
                self.paletteColours.append(paletteColourSelectItem)
            }
            
            self.filteredPaletteColours = self.paletteColours
            // print("[--PaletteViewModel paletteColours should be populated now. With \(self.paletteColours.count) items")
            // print("[--PaletteViewModel paletteColours random element: \(self.paletteColours.randomElement()!)")
        }
    }
    
    // Method to add selected colours to UserDefaults
    func saveSelectedToUserDefaults() {
        let selectedColours: [PaletteColourSelectItem] = self.filteredPaletteColours.filter { $0.isSelected }
        var selectedColoursMarkedAsUserOwned: [PaletteColourSelectItem] = []
        
        for var selectedColour in selectedColours {
            selectedColour.paletteColour.isUserOwned.toggle()
            selectedColoursMarkedAsUserOwned.append(selectedColour)
        }
        
        print("[--CreateUserPaletteViewModel --- selectedColours are: \(selectedColours)")
        
        var coloursToSave: [String: String] = [:]
        for selectedColour in selectedColours {
            coloursToSave[selectedColour.paletteColour.colourName] = selectedColour.paletteColour.hexCode
            print("[--CreateUserPaletteViewModel --- selectedColour in loop: \(selectedColour)")
            print("[--CreateUserPaletteViewModel --- \(selectedColours)")
        }
        
        // Retrieve existing list or create a new one
        if let existingPalettes: [String: String] = UserDefaults.standard.dictionary(forKey: "userPalettes") as? [String: String] {
            // https://stackoverflow.com/a/50532046
            // NOTE: .merge is in place.
            // Another way:
            // let combinedPalette = dict2.forEach { (k,v) in dict1[k] = v }
            let combinedPalette = existingPalettes.merging(coloursToSave) { $1 }
            
            // Save the new list to UserDefaults
            UserDefaults.standard.set(combinedPalette, forKey: "userPalettes")
        } else {
            print("[--CreateUserPaletteViewModel.saveSelectedToUserDefaults() -- couldn't fetch userPalettes")
        }
        
    }
    
    // MARK: Search functionality (DRY AF)
    func filterPaletteColours(term: String) {
        isLoading = true
        self.filteredPaletteColours = self.paletteColours.filter{ $0.paletteColour.colourName.contains(term) }
        print("[--PaletteViewModel filtering paletteColours based on term: \(term). Contains \(self.filteredPaletteColours.count) items.\n \(self.filteredPaletteColours)")
        isLoading = false
    }
        
    func resetFilteredPaletteColours() {
        isLoading = true
        self.filteredPaletteColours = self.paletteColours
        isLoading = false
    }
    
}

// MARK: User Palette VM
// fetch and delete

class UserPaletteViewModel: ObservableObject {
    
    @Published var userPaletteColours: [PaletteColour] = []
    @Published var filteredUserPaletteColours: [PaletteColour] = []
    
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
                    let generatedPaletteColour = PaletteColour(colourName: name, hexCode: hexCode)
                    self.userPaletteColours.append(generatedPaletteColour)
                }
                
                self.filteredUserPaletteColours = self.userPaletteColours // TODO: DRY
            } else {
                // TODO: throw error
                fatalError("failed to retrieve colours from user defaults.")
            }
        } else {
            print("[--UserPaletteViewModel No user defaults initially, user must be on app for first time.")
//            let initialUserPalette: [String: String] = [:]
//            defaults.set(initialUserPalette, forKey: "userPalettes")
            
            // FOR TESTING
            let mockUserPalette: [String: String] = [
                "Viridian": "#40826D",
                "Sienna": "#E97451",
                "Cadmium Red": "#D22B2B",
                "Red Ochre": "#913831",
                "Burnt Umber": "#6E260E",
                "Ultramarine": "#0437F2"
            ]
            
            // display
            let userPaletteColoursAsPalette = mockUserPalette.map { PaletteColour(colourName: $0.key, hexCode: $0.value) }
            self.userPaletteColours = userPaletteColoursAsPalette // TODO: sort alphabetically
            self.filteredUserPaletteColours = self.userPaletteColours // TODO: DRY
            
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
