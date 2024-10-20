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

struct PaletteListItemView: View {
    @State var paletteColourItem: PaletteColour
    var body: some View {
        VStack {
            RoundedRectangle(cornerRadius: 12)
                .fill(Color(paletteColourItem.uiColor))
                .frame(height: 100)
            Text(paletteColourItem.colourName)
        }
        .padding()
    }
}

struct PaletteListView: View {
    @ObservedObject var paletteViewModel: PaletteListViewModel = PaletteListViewModel()
    
    // MARK: Search logic
    @State private var searchText: String = ""
    
    // MARK: VGrid logic
    let columns = Array(repeating: GridItem(.flexible()), count: 3)
    
    var body: some View {
        NavigationStack {
            ScrollView {
                LazyVGrid(columns: self.columns) {
                    ForEach(paletteViewModel.paletteColours) {
                        PaletteListItemView(paletteColourItem: $0)
                    }
                }
                .padding()
            }
        }
        .onAppear {
            Task { print("you're at paletteListView") }
        }
    }
}

#Preview {
    PaletteListView()
}

