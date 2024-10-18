//
//  PaletteViewModel.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-17.
//

import Foundation

/**
 From the colour map, it displays all pairs.
 */
class PaletteViewModel: ObservableObject {
    // displays list of colours

    @Published var palette: [Palette] = []
    
    init() {
        self.fetchPalettte()
    }
    
    /**
     Creates a palette from our in-house map so we can display it to user.
     */
    func fetchPalettte() {
        // get the mapping
        // self.palette = ColourMapper.colourMap
    }
}
