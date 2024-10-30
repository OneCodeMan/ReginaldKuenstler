import Foundation
import SwiftUI

// MARK: Create User Palette VM
// add to palette

class CreateUserPaletteViewModel: ObservableObject {
    @Published var paletteColourSelectItems: [PaletteColourSelectItem] = []
    @Published var filteredPaletteColourSelectItems: [PaletteColourSelectItem] = []
    @Published var isLoading: Bool = false
    @Published var groupedColourSelectItems: [String: [PaletteColourSelectItem]] = [:]
    
    private var userPaletteViewModel: UserPaletteViewModel
    
    init() {
        self.userPaletteViewModel = UserPaletteViewModel()
        fetchUserPalettes()
        Task { try await fetchPaletteColours() }
    }
    
    // Update the initializer to accept userPaletteViewModel
    init(userPaletteViewModel: UserPaletteViewModel) {
        self.userPaletteViewModel = userPaletteViewModel // Store the reference
        print("\nCreateUserPaletteViewModel init() -- FETCHING USER PALETTES FROM USERPALETTEVIEWMODEL")
        fetchUserPalettes()
        Task { try await fetchPaletteColours() }
    }
    
    @MainActor
    func fetchPaletteColours() async throws {
        let colourMap = ColourMapper.shared.colourMap
        let paletteColours: [PaletteColour] = colourMap.map { PaletteColour(fromVColour: $0) }
            
        for var colour in paletteColours {
            if self.userPaletteViewModel.userPaletteColours.contains(colour) {
                colour.isUserOwned = true
            }
            let paletteColourSelectItem = PaletteColourSelectItem(paletteColour: colour, isSelected: false)
            self.paletteColourSelectItems.append(paletteColourSelectItem)
        }

        self.filteredPaletteColourSelectItems = self.paletteColourSelectItems
        self.groupedColourSelectItems = ColourHelper.groupColourSelectItems(colours: self.paletteColourSelectItems)
    }
    
    func fetchUserPalettes() {
        self.userPaletteViewModel.fetchUserPalettes()
    }
    
    func saveSelectedToUserDefaults() {
        let selectedColours = self.filteredPaletteColourSelectItems.filter { $0.isSelected }
        let coloursToSave = selectedColours.reduce(into: [String: String]()) { result, item in
            result[item.paletteColour.colourName] = item.paletteColour.hexCode
        }
        userPaletteViewModel.saveUserPaletteColours(coloursToSave)
    }
    
    func clearUserSelectedColours() {
        for index in filteredPaletteColourSelectItems.indices {
            filteredPaletteColourSelectItems[index].isSelected = false
        }
        self.groupedColourSelectItems = ColourHelper.groupColourSelectItems(colours: filteredPaletteColourSelectItems)
    }
    
    func filterPaletteColours(term: String) {
        isLoading = true
        let filteredItems = paletteColourSelectItems.filter { $0.paletteColour.colourName.contains(term) }
        self.groupedColourSelectItems = ColourHelper.groupColourSelectItems(colours: filteredItems)
        isLoading = false
    }
    
    func resetFilteredPaletteColours() {
        isLoading = true
        self.groupedColourSelectItems = ColourHelper.groupColourSelectItems(colours: paletteColourSelectItems)
        isLoading = false
    }
}
