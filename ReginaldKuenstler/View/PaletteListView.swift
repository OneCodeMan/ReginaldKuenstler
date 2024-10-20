//
//  PaletteListView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-18.
//

/**
 TODOs:
 - Select option to enable between selectMode and viewMode
 - Favourited pigments
 - State for pigments owned
 
 */

import SwiftUI

struct PaletteListView: View {
    @ObservedObject var paletteViewModel: PaletteListViewModel = PaletteListViewModel()
    
    var body: some View {
        VStack {
            // TODO: Search bar
            
            // TODO: List of colours
            /**
             For Each colour in colourMap
                display it (circle colour, title)
             */
            
            
        } // END OF ROOT VSTACK
    }
}

#Preview {
    PaletteListView()
}
