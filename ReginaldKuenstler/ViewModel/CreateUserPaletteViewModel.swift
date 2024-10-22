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
    @Published var paletteColourSelectItems: [PaletteColourSelectItem] = []
    @Published var filteredPaletteColourSelectItems: [PaletteColourSelectItem] = []
    @Published var isLoading: Bool = false
    
    // private variables
    private var userDefaultPalette: [PaletteColour] = []
    
    // ["Red": [], "Green": [], "Blue": [], ...]
    @Published var groupedColourSelectItems: [String: [PaletteColourSelectItem]] = [:]
    
    init() {
        // UserDefaultsHelper.clearUserPaletteFromDefaults()
        fetchUserPalettes()
        Task { try await self.fetchPaletteColours() }
    }
    
    @MainActor
    func fetchPaletteColours(completion: (([VColour]) -> Void)? = nil) async throws {
        let mapper = ColourMapper()
        
        mapper.createColourMapFromCSV { colourMap in
            
            // print("[--PaletteViewModel generateColourMapping() colourMap \(colourMap.count) items")
            
            // take intersection of userPalette and paletteColours
            // on paletterColours, either exclude or change isUserOwned on matching items
            let paletteColours: [PaletteColour] = colourMap.map { PaletteColour(fromVColour: $0) }
            // let intersectionOfUserAndCompletePalette: [PaletteColour] = self.userDefaultPalette.filter { paletteColours.contains($0) }
            
            for var colour in paletteColours {

                if self.userDefaultPalette.contains(colour) {
                    // mark as userOwned
                    colour.isUserOwned = true
                }
                
                let paletteColourSelectItem = PaletteColourSelectItem(paletteColour: colour, isSelected: false)
                self.paletteColourSelectItems.append(paletteColourSelectItem)
            }

            self.filteredPaletteColourSelectItems = self.paletteColourSelectItems
            self.groupedColourSelectItems = ColourHelper.groupColourSelectItems(colours: self.paletteColourSelectItems)
            // print("[--PaletteViewModel paletteColours should be populated now. With \(self.paletteColours.count) items")
            // print("[--PaletteViewModel paletteColours random element: \(self.paletteColours.randomElement()!)")
        }
    }
    
    func fetchUserPalettes() {
        self.userDefaultPalette = []
        let defaults = UserDefaults.standard
        
        if UserDefaultsHelper.isKeyPresentInUserDefaults(key: "userPalettes") {
            print("[--CreateUserPaletteViewModel we have a palette, gonna retrieve them now...")
            if let userPaletteFromUserDefaults = defaults.dictionary(forKey: "userPalettes") as? [String: String]  {
                
                // take the user default palette and convert to PaletteColour objects
                for (name, hexCode) in userPaletteFromUserDefaults {
                    let generatedPaletteColour = PaletteColour(colourName: name, hexCode: hexCode)
                    self.userDefaultPalette.append(generatedPaletteColour)
                }
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
            self.userDefaultPalette = userPaletteColoursAsPalette // TODO: sort alphabetically
            
            // actually add them to user defaults
            defaults.set(mockUserPalette, forKey: "userPalettes")
        }
        
    }
    
    // Method to add selected colours to UserDefaults
    func saveSelectedToUserDefaults() {
        let selectedColours: [PaletteColourSelectItem] = self.filteredPaletteColourSelectItems.filter { $0.isSelected }
        
        // array with selectedColours marked as userOwned
        var selectedColoursMarkedAsUserOwned: [PaletteColourSelectItem] = []
        for var selectedColour in selectedColours {
            selectedColour.paletteColour.isUserOwned = true
            selectedColoursMarkedAsUserOwned.append(selectedColour)
        }
        
        print("[--CreateUserPaletteViewModel --- selectedColours are: \(selectedColours)")
        
        var coloursToSave: [String: String] = [:]
        for selectedColour in selectedColoursMarkedAsUserOwned {
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
        self.filteredPaletteColourSelectItems = self.paletteColourSelectItems.filter{ $0.paletteColour.colourName.contains(term) }
        print("[--PaletteViewModel filtering paletteColours based on term: \(term). Contains \(self.filteredPaletteColourSelectItems.count) items.\n \(self.filteredPaletteColourSelectItems)")
        isLoading = false
    }
        
    func resetFilteredPaletteColours() {
        isLoading = true
        self.filteredPaletteColourSelectItems = self.paletteColourSelectItems
        isLoading = false
    }
    
}

// TODO: put into own file
extension Array
    where Element: Equatable
{
    func intersects(_ other: Array) -> Bool
    {
        for e in other {
            if contains(where: {$0 == e}) {
                return true
            }
        }
        return false
    }
}
