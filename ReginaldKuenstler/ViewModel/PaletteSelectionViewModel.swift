//
//  PaletteViewModel.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import Foundation

/**
 From the colour map, it displays all colours
 SELECTION LIST.
 */
class PaletteListViewModel: ObservableObject {
    // displays list of colours
    @Published var colourMap: [VColour] = []
    @Published var paletteColours: [PaletteColour] = [PaletteColour]()
    @Published var isLoading: Bool = false

    @Published var filteredPaletteColours: [PaletteColour] = [PaletteColour]()
    
    init() {
        self.fetchPaletteColours()
    }
    
    private func fetchPaletteColours(completion: (([VColour]) -> Void)? = nil) {
        let mapper = ColourMapper()
        
        DispatchQueue.main.async {
            mapper.createColourMapFromCSV { colourMap in
                self.colourMap = colourMap
                print("[--PaletteViewModel generateColourMapping() colourMap \(colourMap.count) items")
                // convert the colourMap ([VColour]) to an array of PaletteColours
            }
        }
        
        completion?(self.colourMap)
    }
    
    // MARK: Search functionality
    func filterPaletteColours(term: String) {
        isLoading = true
        self.filteredPaletteColours = self.filteredPaletteColours.filter{ $0.colourName.contains(term) }
        isLoading = false
    }
        
    func resetFilteredPaletteColours() {
        isLoading = true
        self.filteredPaletteColours = self.paletteColours
        isLoading = false
    }
}
