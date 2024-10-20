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
    
    init() {
        self.fetchPigments()
    }
    
    private func fetchPigments(completion: (([VColour]) -> Void)? = nil) {
        let mapper = ColourMapper()
        
        DispatchQueue.main.async {
            mapper.createColourMapFromCSV { colourMap in
                self.colourMap = colourMap
                print("[--PaletteViewModel generateColourMapping() colourMap \(colourMap.count) items")
            }
        }
        
        completion?(self.colourMap)
    }
}
