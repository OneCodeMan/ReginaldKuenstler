//
//  PaletteListView.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-18.
//

// This should only be viewable on "Add to Your Palette" flow

/**
 TODOs:
 - Select option to enable between selectMode and viewMode
 - Favourited pigments
 - State for pigments owned
 -
 
 */

import SwiftUI

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
                    ForEach(paletteViewModel.filteredPaletteColours) {
                        PaletteListItemView(paletteColourItem: $0)
                    }
                }
                .padding()
                .scrollContentBackground(.hidden)
                .searchable(text: $searchText)
                .onChange(of: searchText) { search in
                    if !search.isEmpty {
                        self.paletteViewModel.filterPaletteColours(term: search)
                    } else {
                        self.paletteViewModel.resetFilteredPaletteColours()
                    }
                }
            }
        }
        .onAppear {
            // FIXME: Do we neeed this if vm does this on init?
            // Task { try await self.paletteViewModel.fetchPaletteColours() }
        }
    }
}

#Preview {
    PaletteListView()
}

