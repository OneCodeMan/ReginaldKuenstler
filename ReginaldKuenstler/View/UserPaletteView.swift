//
//  UserPalette.swift
//  ReginaldKuenstler
//
//  Created by Dave Gumba on 2024-10-20.
//

/**
 Either a list of palettes or an empty view.
 The list of palettes comes from UserDefaults.
 */

import SwiftUI

struct UserPaletteView: View {
    @StateObject var userPaletteViewModel = UserPaletteViewModel()
    
    // MARK: search logic
    @State var searchText: String = ""
    
    // MARK: VGrid logic
    let columns = Array(repeating: GridItem(.flexible()), count: 3)
    
    var body: some View {
        NavigationStack {
            VStack {
                // TODO: ADD FUNCTIONALITY. LATER!!
                Text("")
                    .toolbar {
                        NavigationLink(destination: EmptyView()) {
                            Text("Add")
                        }
                    }
                
                // GRID OR EMPTY VIEW
                if !userPaletteViewModel.userPaletteColours.isEmpty {
                    ScrollView {
                        LazyVGrid(columns: self.columns) {
                            ForEach(userPaletteViewModel.filteredUserPaletteColours) {
                                PaletteListItemView(paletteColourItem: $0)
                            }
                        }
                        .padding()
                        .scrollContentBackground(.hidden)
                        .searchable(text: $searchText)
                        .onChange(of: searchText) { search in
                            if !search.isEmpty {
                                self.userPaletteViewModel.filterPaletteColours(term: search)
                            } else {
                                self.userPaletteViewModel.resetFilteredPaletteColours()
                            }
                        }
                    } // end of scrollview
                } else {
                    EmptyView()
                } // else clause end bracket
            } // end of vstack
            .navigationTitle("Your Palette")
        }
            
    }
}

#Preview {
    UserPaletteView()
}
