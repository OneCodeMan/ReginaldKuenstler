import Foundation
import SwiftUI

// MARK: User Palette VM
// fetch and delete

class UserPaletteViewModel: ObservableObject {
    @Published var userPaletteColours: [PaletteColour] = []
    @Published var filteredUserPaletteColours: [PaletteColour] = []
    @Published var groupedColours: [String: [PaletteColour]] = [:]
    @Published var isLoading: Bool = false
    
    // Computed property to return userPaletteColors as a dictionary
    var userPaletteColoursDictionary: [String: String] {
        return userPaletteColours.reduce(into: [String: String]()) { dict, color in
            dict[color.colourName] = color.hexCode
        }
    }
    
    init() {
        fetchUserPalettes()
    }
    
    func fetchUserPalettes() {
        self.userPaletteColours = []
        let defaults = UserDefaults.standard
        
        if let userPaletteFromUserDefaults = defaults.dictionary(forKey: UserPaletteConstants.userPalettesKey) as? [String: String]  {
            for (name, hexCode) in userPaletteFromUserDefaults {
                let generatedPaletteColour = PaletteColour(colourName: name, hexCode: hexCode, isUserOwned: true)
                self.userPaletteColours.append(generatedPaletteColour)
            }
            self.filteredUserPaletteColours = self.userPaletteColours
            self.groupedColours = ColourHelper.groupColours(colours: self.filteredUserPaletteColours)
        } else {
            print("[--UserPaletteViewModel No user defaults initially.")
            // Initialize mock data for first run
            let mockUserPalette: [String: String] = [:]
            self.userPaletteColours = mockUserPalette.map { PaletteColour(colourName: $0.key, hexCode: $0.value) }
            self.filteredUserPaletteColours = self.userPaletteColours
            defaults.set(mockUserPalette, forKey: UserPaletteConstants.userPalettesKey)
        }
    }
    
    func saveUserPaletteColours(_ newColours: [String: String]) {
        let combinedPalette = userPaletteColoursDictionary.merging(newColours) { $1 }
        UserDefaults.standard.set(combinedPalette, forKey: UserPaletteConstants.userPalettesKey)
        self.userPaletteColours = combinedPalette.map { PaletteColour(colourName: $0.key, hexCode: $0.value) }
    }
    
    // MARK: Delete functionality
    func deletePaletteColourFromUserPalette(paletteColour pc: PaletteColour, groupName: String) {
        if let index = groupedColours[groupName]?.firstIndex(of: pc) {
            groupedColours[groupName]?.remove(at: index)
            let updatedData = groupedColours.flatMap { $0.value }.reduce(into: [String: String]()) {
                $0[$1.colourName] = $1.hexCode
            }
            UserDefaults.standard.set(updatedData, forKey: UserPaletteConstants.userPalettesKey)
            fetchUserPalettes() // Refresh the palettes after deletion
        }
    }
    
    func deleteAllColoursFromUserPalette() {
        UserDefaults.standard.removeObject(forKey: UserPaletteConstants.userPalettesKey)
        fetchUserPalettes()
    }
    
    // MARK: Search functionality
    func filterPaletteColours(term: String) {
        isLoading = true
        self.filteredUserPaletteColours = self.userPaletteColours.filter { $0.colourName.contains(term) }
        self.groupedColours = ColourHelper.groupColours(colours: self.filteredUserPaletteColours)
        isLoading = false
    }
    
    func resetFilteredPaletteColours() {
        isLoading = true
        self.filteredUserPaletteColours = self.userPaletteColours
        self.groupedColours = ColourHelper.groupColours(colours: self.userPaletteColours)
        isLoading = false
    }
}
