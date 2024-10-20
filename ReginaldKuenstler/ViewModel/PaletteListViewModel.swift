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
    @Published var isLoading: Bool = false

    // original palette colours copy, contains all
    @Published var paletteColours: [PaletteColour] = [PaletteColour]()
    
    // what we're displaying to the user.
    @Published var filteredPaletteColours: [PaletteColour] = [PaletteColour]()
    
    init() {
        Task { try await self.fetchPaletteColours() }
    }
    
    @MainActor
    func fetchPaletteColours(completion: (([VColour]) -> Void)? = nil) async throws {
        let mapper = ColourMapper()
        
        mapper.createColourMapFromCSV { colourMap in
            self.colourMap = colourMap
            
            print("[--PaletteViewModel generateColourMapping() colourMap \(colourMap.count) items")
            
            // convert the colourMap ([VColour]) to an array of PaletteColours
            for vColour in colourMap {
                let generatedPaletteColour = PaletteColour(fromVColour: vColour)
                self.paletteColours.append(generatedPaletteColour)
            }
            
            // initially, filteredPaletteColours has all the colours.
            self.filteredPaletteColours = self.paletteColours
            print("[--PaletteViewModel paletteColours should be populated now. With \(self.paletteColours.count) items")
            print("[--PaletteViewModel paletteColours random element: \(self.paletteColours.randomElement()!)")
        }
        
        completion?(self.colourMap)
    }
    
    // MARK: Search functionality
    func filterPaletteColours(term: String) {
        isLoading = true
        self.filteredPaletteColours = self.paletteColours.filter{ $0.colourName.contains(term) }
        print("[--PaletteViewModel filtering paletteColours based on term: \(term). Contains \(self.filteredPaletteColours.count) items.\n \(self.filteredPaletteColours)")
        isLoading = false
    }
        
    func resetFilteredPaletteColours() {
        isLoading = true
        self.filteredPaletteColours = self.paletteColours
        isLoading = false
    }
}
